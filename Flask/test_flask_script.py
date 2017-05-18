#coding=utf8
"""
命令行扩展flask-script
Flask开发的Web服务器支持很多启动设置选项，但只能在脚本中作为参数传给app.run()函数。这种方式并不十分方便，传递设置选项的理想方式是使用命令行参数。
Flask-Script是一个Flask扩展，为Flask程序添加了一个命令行解析器。Flask-Script自带了一组常用选项，而且还支持自定义命令。

pip install flask-script
"""

#from flask.ext.script import Manager  #专为Flask开发的扩展都暴漏在flask.ext命名空间下
from flask_script import Manager
from flask import Flask
from flask import request


app = Flask(__name__)
manager = Manager(app)  #把程序实例作为参数传给构造函数

@app.route('/')  #路由
def index():  #视图函数
    return '<h1>Hello World!</h1>', 200

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name


@app.route('/too')
def too():
    user_agent = request.headers.get('User-Agent')
    print request.headers
    return '<p>Your Browser is %s</p>' % user_agent

if __name__ == '__main__':
    manager.run()  #由manager.run()启动后就能解析命令行了



"""
shell命令用于在程序的上下文中启动Python shell会话。可以使用这个会话中运行维护任务或测试，还可调试异常
runserver将以调试模式启动Web服务器，支持很多选项

python test_ext1.py
python test_ext1.py runserver --help
python test_ext1.py shell --help
"""
