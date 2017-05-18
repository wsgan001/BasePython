#coding=utf8
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

#解决问题：因为程序在全局作用域中创建时无法动态修改配置
#解决方法：延迟创建程序实例，把创建过程移到可显式调用的工厂函数中。这种方法不仅可以给脚本留出配置程序的时间，还能够创建多个程序实例
#工厂函数
def create_app(config_name): #参数是程序使用的配置名
    app = Flask(__name__)
    app.config.from_object(config[config_name]) #config.py文件中定义的配置可以使用Flask的app.config配置对象提供的from_object()方法直接导入程序
    config[config_name].init_app(app)  #初始化

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)  #注册蓝本

    return app

