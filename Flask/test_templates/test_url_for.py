#coding=utf8
"""
为编写动态路由
Flask提供了url_for()辅助函数(模板中使用)，它可以使用程序URL映射中保存的信息生成URL

url_for()函数最简单的用法是以视图函数名(或者app.add_url_route() 定义路由时使用 的端点名)作为参数，返回对应的URL
例如，在当前版本的hello.py程序中调用：
url_ for('index') 得到的结果是/
url_for('index', _external=True) 返回的则是绝对地址http://localhost:5000/

url_for('user', name='john', _external=True) 返回结果是 http://localhost:5000/user/john
url_for('index', page=2) 返回结果是 /?page=2
url_for('static', filename='css/styles.css', _external=True) 得到的结果是 http://localhost:5000/static/css/styles.css

"""


from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap

app = Flask(__name__)

manager = Manager(app)
bootstrap = Bootstrap(app)


@app.route('/user/<name>')
def user(name):
    return render_template('user4.html', name=name)


if __name__ == '__main__':
    manager.run()
