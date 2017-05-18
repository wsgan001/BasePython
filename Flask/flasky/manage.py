#!/usr/bin/env python
#coding=utf8
import os
COV = None  #检测引擎
'''
coverage:代码覆盖工具
coverage.coverage()用于启动覆盖检测引擎。branch=True选项开启分支覆盖分析， 除了跟踪哪行代码已经执行外，还要检查每个条件语句的True分支和False分支是否都执
行了。include选项用来限制程序包中文件的分析范围，只对这些文件中的代码进行覆盖检测。如果不指定include选项，虚拟环境中安装的全部扩展和测试代码都会包含进覆盖
报告中，给报告添加很多杂项

pip install coverage
'''
if os.environ.get('FLASK_COVERAGE'):
    import coverage
    COV = coverage.coverage(branch=True, include='app/*')
    COV.start()

from app import create_app, db
from app.models import User, Follow, Role, Permission, Post, Comment
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User, Follow=Follow, Role=Role,
                Permission=Permission, Post=Post, Comment=Comment)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

#测试
@manager.command
def test(coverage=False):
    """Run the unit tests."""
    if coverage and not os.environ.get('FLASK_COVERAGE'):
        import sys
        os.environ['FLASK_COVERAGE'] = '1'
        os.execvp(sys.executable, [sys.executable] + sys.argv)
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    if COV:
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, 'tmp/coverage')
        COV.html_report(directory=covdir)
        print('HTML version: file://%s/index.html' % covdir)
        COV.erase()
'''
执行：python manage.py test --coverage
在终端输出报告，同时还会生成一个使用HTML编写精美报告并写入硬盘
'''


#分析源码: 为每条请求启用Python分析器
#分析器监视运行中的程序，记录调用的函数以及运行各函数所消耗的时间，然后生成一份详细的报告，指出运行最慢的函数
@manager.command
def profile(length=25, profile_dir=None):
    """Start the application under the code profiler."""
    from werkzeug.contrib.profiler import ProfilerMiddleware
    app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[length],
                                      profile_dir=profile_dir)
    app.run()
'''
执行： python manage.py profile
'''


#部署
#如果每次安装或升级程序都手动执行任务，那么容易出错也浪费时间，所以可以在manage.py中添加一个命令自动执行所需操作
@manager.command
def deploy():
    """Run deployment tasks."""
    from flask_migrate import upgrade
    from app.models import Role, User

    # migrate database to latest revision   把数据库迁移到最新修订版本
    upgrade()

    # create user roles 创建用户角色
    Role.insert_roles()

    # create self-follows for all users  让所有用户都关注此用户
    User.add_self_follows()


if __name__ == '__main__':
    manager.run()
