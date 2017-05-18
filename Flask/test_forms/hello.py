#coding=utf8
"""
Flask-WTF扩展处理Web表单。这个扩展对独立的WTForms包进行了包装，方便集成到Flask程序中

pip install flask-wtf
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment


app = Flask(__name__)

#app.config字典可用来存储框架、扩展和程序本身的配置变量
app.config['SECRET_KEY'] = 'hard to guess string'  #跨站请求伪造保护通用密钥   Flask-WTF 使用这个密钥生成加密令牌，再用令牌验证请求中表单数据的真伪

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


'''
每个Web表单都由一个继承自Form的类表示。这个类定义表单中的一组字段，每个字段都用对象表示。字段对象可附属一个或多个验证函数。验证函数用来验证用户提交的输入
值是否符合要求
'''
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():  #提交表单后，如果数据能被所有验证函数接受，那么validate_on_submit()方法的返回值为True，否则返回False
        name = form.name.data
        form.name.data = ''  #清空表单字段
        print 111111
    print 222222
    return render_template('index.html', form=form, name=name)


if __name__ == '__main__':
    manager.run()
