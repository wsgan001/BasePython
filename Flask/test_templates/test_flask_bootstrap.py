#coding=utf8
"""
集成Bootstrap
Bootstrap是Twitter开发的一个开源框架，它提供的用户界面组件可用于创建整洁且具有吸引力的网页
要想在程序中集成Bootstrap，显然要对模板做所有必要的改动。不过，更简单的方法是 使用一个名为Flask-Bootstrap的Flask扩展，简化集成的过程

pip install flask-bootstrap
"""
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask import Flask, render_template

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app) #初始化Flask-Bootstrap之后，就可以在程序中使用一个包含所有Bootstrap文件的基模板user2.html


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user2.html', name=name)


if __name__ == '__main__':
    manager.run()
