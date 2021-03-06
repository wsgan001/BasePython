#coding=utf8
from flask import render_template, session, redirect, url_for, current_app
from .. import db
from ..models import User
from ..email import send_email
from . import main
from .forms import NameForm

#使用蓝本的route修饰器（而非app的）
@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
            if current_app.config['FLASKY_ADMIN']:
                send_email(current_app.config['FLASKY_ADMIN'], 'New User',
                           'mail/new_user', user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('.index'))  #参数需要带命名空间(蓝本名): url_for('main.index')   同一蓝本中可以使用简写形式: url_for('.index')
    return render_template('index.html',
                           form=form, name=session.get('name'),
                           known=session.get('known', False))
