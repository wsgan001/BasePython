#coding=utf8
"""
版本3：
让用户知道状态发生了变化。可以使用确认消息、警告或者错 误提醒。一个典型例子是，用户提交了有一项错误的登录表单后，服务器发回的响应重新 渲染了登录表单，
并在表单上面显示一个消息，提示用户用户名或密码错误。flash()函数可实现这种效果

渲染消息
在基模板base2.html中使用Flask的get_flashed_ messages()函数获取并渲染消息
使用循环是因为在之前的请求循环中每次调用flash()函数时都会生成一个消息，所以可能有多个消息在排队等待显示。get_flashed_messages()函数获取的消息在下次调
用时不会再次返回，因此Flash消息只显示一次，然后就消失了
"""

from flask import Flask, render_template, session, redirect, url_for, flash
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404_2.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500_2.html'), 500


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        print 11111
        if old_name is not None and old_name != form.name.data:
            print 22222
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    print 33333
    return render_template('index2.html', form=form, name=session.get('name'))


if __name__ == '__main__':
    manager.run()
