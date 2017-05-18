#coding=utf8
'''
werkzeug不是一个web框架，是http和WSGI相关的工具集，可以作为一个Web框架的底层库，提供了python web WSGI开发相关的功能：
路由处理： 怎么根据请求中的url找到它的处理函数
request和response封装： 更好的读取请求的数据，也更容易生成响应
一个自带的WSGI server：可以用来测试环境运行自己的应用
还是实现了很多非常有用的数据结构和函数

pip install Werkzeug
'''


#用werkzeug编写的一个简单的hello world的WSGI APP
from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple


class APP(object):
    def application(self, environ, start_response):
        request = Request(environ)
        text = 'Hello %s' % request.args.get('name','World')
        response = Response(text, mimetype='text/plain')
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.application(environ, start_response)


if __name__ == '__main__':
    app = APP()
    run_simple('127.0.0.1', 8011, app, use_debugger=True, use_reloader=True)  #低层还是HTTPServer实现的
