#coding=utf8
"""
版本2：使用重定向和用户会话
可解决版本1中在表单页面，浏览器刷新会再次提交表单而出现警告

"""

from flask import Flask, render_template, session, redirect, url_for
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
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():       #首次或重定向后validate_on_submit为false
        session['name'] = form.name.data   #保存到用户会话中
        print 111111
        return redirect(url_for('index'))   #使用url_for保证URL和定义的路由兼容
    print 222222
    return render_template('index.html', form=form, name=session.get('name'))


if __name__ == '__main__':
    manager.run()
