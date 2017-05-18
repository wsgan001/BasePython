#coding=utf8
"""
Flask的认证扩展:
Flask-Login: 管理已登录用户的用户会话
Werkzeug: 计算密码散列值并进行核对
itsdangerous: 生成并核对加密安全令牌

generate_password_hash(password, method=pbkdf2:sha1, salt_length=8):这个函数将原始密码作为输入，以字符串形式输出密码的散列值，输出的值可保存在用户数
据库中。 method和salt_length的默认值就能满足大多数需求。
check_password_hash(hash, password): 这个函数的参数是从数据库中取回的密码散列值和用户输入的密码。返回值为True 表明密码正确。

pip install flask-login
"""

from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from . import db, login_manager
from flask_login import UserMixin



class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(UserMixin, db.Model):  #继承Flask-Login提供的UserMixin类，采用默认实现Flask-Login要求实现的用户方法
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)   #添加email字段,用作用户使用电子邮件地址登录
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean, default=False)  #保存账户的确认状态

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter  #password为只写属性
    def password(self, password):
        self.password_hash = generate_password_hash(password)   #相同的密码，它们的密码散列值也完全不一样

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    #生成一个令牌，有效期默认为一小时
    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)  #TimedJSONWebSignatureSerializer类生成具有过期时间的JSON Web签名
        return s.dumps({'confirm': self.id})  #为指定的数据生成一个加密签名，然后再对数据和签名进行序列化，生成令 牌字符串

    #检验令牌，如果检验通过，则把新添加的confirmed属性设为True
    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:  #检查令牌中的id是否和存储在current_user中的已登录用户匹配
            return False
        self.confirmed = True
        db.session.add(self)

    def __repr__(self):
        return '<User %r>' % self.username


    def generate_reset_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'reset': self.id})

    def reset_password(self, token, new_password):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('reset') != self.id:
            return False
        self.password = new_password
        db.session.add(self)
        return True

    def generate_email_change_token(self, new_email, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'change_email': self.id, 'new_email': new_email})

    def change_email(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('change_email') != self.id:
            return False
        new_email = data.get('new_email')
        if new_email is None:
            return False
        if self.query.filter_by(email=new_email).first() is not None:
            return False
        self.email = new_email
        db.session.add(self)
        return True


#Flask-Login要求程序实现一个回调函数，使用指定的标识符加载用户
#接收以Unicode字符串形式表示的用户标识符。如果能找到用户，这个函数必须返回用户对象;否则应该返回None
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


