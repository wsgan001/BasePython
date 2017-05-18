#coding=utf8
'''
Flask测试客户端
程序的某些代码严重依赖运行中的程序所创建的环境。例如不能直接调用视图函数中的代码进行测试，因为这个函数可能需要访问Flask上下文全局变量，如request或session;
视图函数可能还等待接收POST请求中的表单数据，而且某些视图函数要求用户先登录。简而言之，视图函数只能在请求上下文和运行中的程序里运行。

测试客户端能复现程序运行在Web服务器中的环境，让测试扮演成客户端从而发送请求
'''

import re
import unittest
from flask import url_for
from app import create_app, db
from app.models import User, Role

#使用Flask测试客户端编写的测试框架
class FlaskClientTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        Role.insert_roles()
        self.client = self.app.test_client(use_cookies=True)  #Flask测试客户端对象

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    #演示测试客户端的作用
    def test_home_page(self):
        response = self.client.get(url_for('main.index'))  #get
        self.assertTrue(b'Stranger' in response.data)

    #使用Flask测试客户端模拟新用户注册的整个流程
    def test_register_and_login(self):
        # register a new account 注册新账户
        response = self.client.post(url_for('auth.register'), data={  #post
            'email': 'john@example.com',
            'username': 'john',
            'password': 'cat',
            'password2': 'cat'
        })
        self.assertTrue(response.status_code == 302)

        # login with the new account  使用新注册的账户登录
        response = self.client.post(url_for('auth.login'), data={
            'email': 'john@example.com',
            'password': 'cat'
        }, follow_redirects=True)  #参数follow_redirects=True 自动向重定向
        self.assertTrue(re.search(b'Hello,\s+john!', response.data))
        self.assertTrue(
            b'You have not confirmed your account yet' in response.data)

        # send a confirmation token  发送确认令牌
        user = User.query.filter_by(email='john@example.com').first()
        token = user.generate_confirmation_token()
        response = self.client.get(url_for('auth.confirm', token=token),
                                   follow_redirects=True)
        self.assertTrue(
            b'You have confirmed your account' in response.data)

        # log out  退出
        response = self.client.get(url_for('auth.logout'), follow_redirects=True)
        self.assertTrue(b'You have been logged out' in response.data)
