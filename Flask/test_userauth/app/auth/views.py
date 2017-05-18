#coding=utf8
#认证auth功能的蓝本
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from . import auth
from ..models import User
from ..email import send_email
from .forms import LoginForm, RegistrationForm, ChangePasswordForm, PasswordResetRequestForm, PasswordResetForm, ChangeEmailForm
from .. import db


@auth.before_app_request  #before_app_request修饰器：在蓝本中使用针对程序全局请求的钩子
def before_request():
    '''
    使用Flask提供的before_request钩子(只能应用到属于蓝本的请求上)：决定用户确认账户之前可以做哪些操作
    过滤未确认的账户: 未确认的用户登录只显示一个页面，这个页面要求用户在获取权限之前先确认账户
    '''
    if current_user.is_authenticated \
            and not current_user.confirmed \
            and request.endpoint \
            and request.endpoint[:5] != 'auth.' \
            and request.endpoint != 'static':
        return redirect(url_for('auth.unconfirmed'))


@auth.route('/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous or current_user.confirmed:
        return redirect(url_for('main.index'))
    return render_template('auth/unconfirmed.html')
'''
同时满足以下3个条件时，before_app_request处理程序会拦截请求(被重定向到/auth/unconfirmed路由，显示一个确认账户相关信息的页面)
(1) 用户已登录(current_user.is_authenticated()返回True)。
(2) 用户的账户还未确认。
(3) 请求的端点(使用request.endpoint获取)不在认证蓝本中
'''


#登入用户
@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            '''
            调用Flask-Login中的login_user()函数，在用户会话中把用户标记为已登录。login_user()函数的参数是要登录的用户，以及可选的“记住我”布尔值，记住
            我”也在表单中填写。如果值为False，那么关闭浏览器后用户会话就过期了，所以下次用户访问时要重新登录。如果值为True，那么会在用户浏览器中写入一个
            长期有效的cookie，使用这个cookie可以复现用户会话
            '''
            login_user(user, form.remember_me.data)

            '''
            用户访问未授权的URL时会显示登录表单，Flask-Login会把原地址保存在查询字符串的next参数中，这个参数可从request.args字典中读取, 如果查询字符串中没有
            next参数，则重定向到首页
            '''
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password.')  #如果用户输入的电子邮件或密码不正确，程序会设定一个Flash消息，再次渲染表单，让用户重试登录
    return render_template('auth/login.html', form=form)


#登出用户
@auth.route('/logout')
@login_required  #login_required修饰器用于保护路由，如果未认证的用户访问这个路由，Flask-Login会拦截请求，把用户发往登录页面
def logout():
    logout_user()  #调用Flask-Login中的logout_user()函数，删除并重设用户会话
    flash('You have been logged out.')  #显示一个Flash消息，确认这次操作
    return redirect(url_for('main.index'))   #重定向到首页


#注册
@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()  #确认令牌需要用到id，所以不能延后提交
        token = user.generate_confirmation_token()
        send_email(user.email, 'Confirm Your Account',
                   'auth/email/confirm', user=user, token=token)
        flash('You can now login.')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)


#确认用户账户
@auth.route('/confirm/<token>')
@login_required  #保护这个路由，用户点击确认邮件中的链接后，要先登录，然后才能执行这个视图函数
def confirm(token):
    if current_user.confirmed:   #检查已登录的用户是否已经确认过，如果确认过，则重定向到首页
        return redirect(url_for('main.index'))
    if current_user.confirm(token):  #令牌确认 调用confirm()方法（models中定义的），根据确认结果显示不同的Flash消息
        flash('You have confirmed your account. Thanks!')
    else:
        flash('The confirmation link is invalid or has expired.')
    return redirect(url_for('main.index'))

#重新发送账户确认邮件
@auth.route('/confirm')
@login_required
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    send_email(current_user.email, 'Confirm Your Account',
               'auth/email/confirm', user=current_user, token=token)
    flash('A new confirmation email has been sent to you by email.')
    return redirect(url_for('main.index'))


#修改密码
@auth.route('/change-password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        if current_user.verify_password(form.old_password.data):
            current_user.password = form.password.data
            db.session.add(current_user)
            flash('Your password has been updated.')
            return redirect(url_for('main.index'))
        else:
            flash('Invalid password.')
    return render_template("auth/change_password.html", form=form)



#重设密码
@auth.route('/reset', methods=['GET', 'POST'])
def password_reset_request():
    if not current_user.is_anonymous:
        return redirect(url_for('main.index'))
    form = PasswordResetRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            token = user.generate_reset_token()
            send_email(user.email, 'Reset Your Password',
                       'auth/email/reset_password',
                       user=user, token=token,
                       next=request.args.get('next'))
        flash('An email with instructions to reset your password has been '
              'sent to you.')
        return redirect(url_for('auth.login'))
    return render_template('auth/reset_password.html', form=form)


@auth.route('/reset/<token>', methods=['GET', 'POST'])
def password_reset(token):
    if not current_user.is_anonymous:
        return redirect(url_for('main.index'))
    form = PasswordResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            return redirect(url_for('main.index'))
        if user.reset_password(token, form.password.data):
            flash('Your password has been updated.')
            return redirect(url_for('auth.login'))
        else:
            return redirect(url_for('main.index'))
    return render_template('auth/reset_password.html', form=form)


#修改邮箱地址
@auth.route('/change-email', methods=['GET', 'POST'])
@login_required
def change_email_request():
    form = ChangeEmailForm()
    if form.validate_on_submit():
        if current_user.verify_password(form.password.data):
            new_email = form.email.data
            token = current_user.generate_email_change_token(new_email)
            send_email(new_email, 'Confirm your email address',
                       'auth/email/change_email',
                       user=current_user, token=token)
            flash('An email with instructions to confirm your new email '
                  'address has been sent to you.')
            return redirect(url_for('main.index'))
        else:
            flash('Invalid email or password.')
    return render_template("auth/change_email.html", form=form)


@auth.route('/change-email/<token>')
@login_required
def change_email(token):
    if current_user.change_email(token):
        flash('Your email address has been updated.')
    else:
        flash('Invalid request.')
    return redirect(url_for('main.index'))



