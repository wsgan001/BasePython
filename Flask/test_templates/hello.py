#coding=utf8
"""
模板是一个包含响应文本的文件，其中包含用占位变量表示的动态部分，其具体值只在请求的上下文中才能知道。使用真实值替换变量，再返回最终得到的响应字符串，
这一过程称为渲染。为了渲染模板，Flask使用了一个名为Jinja2的强大模板引擎
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') #render_template函数的第一个参数是模板的文件名。随后的参数都是键值对，表示模板中变量对应的真实值


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)

