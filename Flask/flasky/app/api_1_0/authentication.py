#coding=utf8
'''
Flask-HTTP Auth认证用户

pip install flask-httpauth
'''


from flask import g, jsonify
from flask_httpauth import HTTPBasicAuth
from ..models import User, AnonymousUser
from . import api
from .errors import unauthorized, forbidden

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(email_or_token, password):  #验证密令
    if email_or_token == '':
        g.current_user = AnonymousUser()
        return True
    if password == '':
        g.current_user = User.verify_auth_token(email_or_token)  #使用User模型中现有的verify_auth_token方法验证电子邮件地址或认证令牌
        g.token_used = True   #g.token_used变量让视图函数能区分认证方法
        return g.current_user is not None
    user = User.query.filter_by(email=email_or_token).first()
    if not user:
        return False
    g.current_user = user
    g.token_used = False
    return user.verify_password(password)   #使用User模型中现有的verify_password方法验证

'''
如果认证密令不正确，服务器向客户端返回401错误, 默认情况下，Flask-HTTPAuth自动生成这个状态码，但为了和API返回的其他错误保持一致，可以自定义这个错误响应
'''
@auth.error_handler
def auth_error():
    return unauthorized('Invalid credentials')


@api.before_request
@auth.login_required  #保护路由  在before_request处理程序中使用一次login_required修饰器应用到整个蓝本
def before_request():
    if not g.current_user.is_anonymous and \
            not g.current_user.confirmed:   #拒绝已通过认证但没有确认账户的用户
        return forbidden('Unconfirmed account')


#把认证令牌发送给客户端的路由(添加到API蓝本)
@api.route('/token')
def get_token():
    if g.current_user.is_anonymous or g.token_used:
        return unauthorized('Invalid credentials')
    return jsonify({'token': g.current_user.generate_auth_token(
        expiration=3600), 'expiration': 3600})





