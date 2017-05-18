#coding=utf8
"""
Flask-SQLAlchemy是一个Flask扩展，简化了在Flask程序中使用SQLAlchemy的操作。SQLAlchemy是一个很强大的关系型数据库框架，支持多种数据库后台。SQLAlchemy提供
了高层ORM，也提供了使用数据库原生SQL的低层功能


pip install flask-sqlalchemy
"""

import os
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')  #URL必须保存到Flask配置对象的SQLALCHEMY_DATABASE_URI键中
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True  #设为True时每次请求结束后都会自动提交数据库中的变动
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)


#模型（对应数据库表）
class Role(db.Model):
    __tablename__ = 'roles'   #表名
    id = db.Column(db.Integer, primary_key=True)  #属性（对应数据库表中的列）
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')
    '''
    添加到Role模型中的users属性代表这个关系的面向对象视角。对于一个Role类的实例， 其users属性将返回与角色相关联的用户组成的列表
    db.relationship()的第一个参数表明这个关系的另一端是哪个模型
    backref参数向User模型中添加一个role属性，从而定义反向关系
    '''

    def __repr__(self):     #可选
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))  #外键  db.ForeignKey()的参数'roles.id'表明，这列的值是roles表中行的id值

    def __repr__(self):
        return '<User %r>' % self.username

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
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))


if __name__ == '__main__':
    #db.drop_all()   #删除数据库表
    db.create_all()  #创建数据库表
    manager.run()
