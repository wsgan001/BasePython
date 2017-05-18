#coding=utf8
"""
集成moment
moment.js: JavaScript开发的优秀客户端开源代码库，可以在浏览器中渲染日期和时间
Flask-Moment是一个Flask程序扩展，能把moment.js集成到Jinja2模板中

pip install flask-moment
"""

from datetime import datetime
from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
    return render_template('index3.html',
                           current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    return render_template('user5.html', name=name)


if __name__ == '__main__':
    manager.run()


"""
模板中使用的moment的方法说明：
format('LLL') 根据客户端电脑中的时区和区域设置渲染日期和时间。参数决定了渲染的方式，'L' 到 'LLLL' 分别对应不同的复杂度。format()函数还可接受自定义的格式说明符
fromNow() 渲染相对时间戳，而且会随着时间的推移自动刷新显示的时间。这个时间戳最开始显示为“a few seconds ago”，但指定refresh参数后，其内容会随着时间的推移
而更新。如果一直待在这个页面，几分钟后，会看到显示的文本变成“a minute ago”“2 minutes ago”等

fromTime()
calendar()
valueOf()
unix()
"""







