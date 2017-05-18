#coding=utf8
'''
UI模块： 封装模板中包含的标记、样式以及行为的可复用组件
模块本身是一个继承自Tornado的UIModule类的简单Python类，并定义了一个render方法。当一个模板使用{% module Foo(...) %}标签引用一个模块时，Tornado的模板引擎
调用模块的render方法，然后返回一个字符串来替换模板中的模块标签
'''
import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
import os.path

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('hello.html')

class HelloModule(tornado.web.UIModule):  #模块
    def render(self):
        return '<h1>Hello, world hehe!</h1>'

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r'/', HelloHandler)],
        template_path=os.path.join(os.path.dirname(__file__), 'templates'),
        ui_modules={'Hello': HelloModule} #为了在模板中引用模块，必须在应用的设置中声明它。ui_moudles参数期望一个模块名为键、类为值的字典
    )
    server = tornado.httpserver.HTTPServer(app)
    server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
