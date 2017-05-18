#coding=utf8
from flask import Flask
from flask import request
from flask import current_app
from flask import make_response
from flask import redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    response = make_response('<h1>Home, %s</h1>' % current_app.name, 202)  #make_response用于制作response对象
    response.set_cookie('answer', '42')  #设置cookie
    return response

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''


@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'

@app.route('/red')
def index():
  return redirect("http://www.baidu.com")   #重定向

@app.route('/user/<uid>')
def get_user(uid):
  if uid not in ['1','2','3','4','5']:
    abort(404)     #处理错误   控制权交个web服务器而非调用它的函数
  return 'crrect'

if __name__ == '__main__':
    app.run()




