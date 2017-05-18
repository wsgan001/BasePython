#coding=utf8
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()


login_manager = LoginManager()
#session_protection属性可以设为None、'basic' 或 'strong'，以提供不同的安全等级防止用户会话遭篡改。设为'strong'时，Flask-Login会记录客户端IP地址和
#浏览器的用户代理信息，如果发现异动就登出用户
login_manager.session_protection = 'strong'
#login_view属性设置登录页面的端点。前面加上蓝本的名字
login_manager.login_view = 'auth.login'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    #Flask-Login在工厂函数中初始化
    login_manager.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    """
    新增的auth蓝本注册到app
    注册蓝本时使用的url_prefix是可选参数。如果使用了这个参数，注册后蓝本中定义的所有路由都会加上指定的前缀，即这个例子中的/auth
    例如，/login路由会注册成/auth/login
    """
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app


