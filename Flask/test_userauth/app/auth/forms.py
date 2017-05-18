#coding=utf8
#登录表单 包含一个用于输入电子邮件地址的文本字段、一个密码字段、一 个“记住我”复选框和提交按钮

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                             Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')



class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                           Email()])
    #Regexp验证函数，确保username字段只包含字母、数字、 下划线和点号。这个验证函数中正则表达式后面的两个参数分别是正则表达式的旗标和验证失败时显示的错误消息
    username = StringField('Username', validators=[
        Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          'Usernames must have only letters, numbers, dots or underscores')])

    #EqualTo验证函数要附属到两个密码字段中 的一个上，另一个字段则作为参数传入。验证两次密码是否一致
    password = PasswordField('Password', validators=[
        Required(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[Required()])
    submit = SubmitField('Register')

    #如果表单类中定义了以validate_开头且后面跟着字段名的方法，这个方法就和常规的验证函数一起调用
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():  #确保填写的值在数据库中没出现过
            raise ValidationError('Email already registered.') #确保填写的值在数据库中没出现过

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():  #确保填写的值在数据库中没出现过
            raise ValidationError('Username already in use.')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Old password', validators=[Required()])
    password = PasswordField('New password', validators=[
        Required(), EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm new password', validators=[Required()])
    submit = SubmitField('Update Password')



class PasswordResetRequestForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                             Email()])
    submit = SubmitField('Reset Password')


class PasswordResetForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                             Email()])
    password = PasswordField('New Password', validators=[
        Required(), EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm password', validators=[Required()])
    submit = SubmitField('Reset Password')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first() is None:
            raise ValidationError('Unknown email address.')

class ChangeEmailForm(FlaskForm):
    email = StringField('New Email', validators=[Required(), Length(1, 64),
                                                 Email()])
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField('Update Email Address')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')



