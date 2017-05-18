#coding=utf8
from flask import Flask
from flask import request

app = Flask(__name__)  #参数：程序主模块或包的名字，这个参数决定程序的根目录

@app.route('/')  #路由
def index():  #视图函数
    return '<h1>Hello World!</h1>', 200   #第二个参数：状态码（数字）   第三个参数：由首部组成的字典

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name


@app.route('/too')
def too():
    user_agent = request.headers.get('User-Agent')
    #print request.headers
    return '<p>Your Browser is %s</p>' % user_agent

if __name__ == '__main__':
    app.run(debug=True)  #Flask自带的Server在本地端口5000上监听
    #app.run()
