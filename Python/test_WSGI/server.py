#coding=utf8
"""
WSGI（Web Server Gateway Interface）不是服务器，不是API，不是Python模块，更不是什么框架，而是一种服务器和客户端交互的接口规范PEP333！ 一套web server和web框架/web应用之间的协议
"""

from wsgiref.simple_server import make_server


#只要求Web开发者实现一个函数，就可以响应HTTP请求
def application(environ, start_response):
    '''
    application()函数就是符合WSGI标准的一个HTTP处理函数，它接收两个参数：
    environ：一个包含所有HTTP请求信息的dict对象
    start_response：一个发送HTTP响应的函数
    '''
    method = environ['REQUEST_METHOD']
    path = environ['PATH_INFO']
    print 'method:', method
    print 'path:', path

    start_response('200 OK', [('Content-Type', 'text/html')])    #只能调用一次start_response()函数。接收两个参数，一个是HTTP响应码，一个是一组list表示的HTTP Header，每个Header用一个包含两个str的tuple表示
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]


#创建一个服务器，IP地址为空，端口是8000，处理函数是application
httpd = make_server('', 8800, application)
print('Serving HTTP on port 8800...')

#监听HTTP请求
httpd.serve_forever()
