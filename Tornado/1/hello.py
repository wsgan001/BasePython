#coding=utf8

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

#命令行默认参数及类型
define("port", default=8000, help="run on the given port", type=int)

#处理器
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Hello') #从一个查询字符串中取得参数greeting的值（如果这个参数没有出现在查询字符串中，Tornado将使用get_argument的第二个参数作为默认值）
        self.set_status(200) #可以使用RequestHandler类的set_status()方法显式地设置HTTP状态码
        self.write(greeting + ', friendly user!\n') #以一个字符串作为函数的参数，并将其写入到HTTP响应中

    #重写错误响应
    def write_error(self, status_code, **kwargs):
        self.write("Gosh darnit, user! You caused a %d error.\n" % status_code)

if __name__ == "__main__":
    #套路：
    #解析命令行
    tornado.options.parse_command_line()

    #通过处理器handler获得app（Application类的实例 传递给Application类__init__方法的最重要的参数是handlers。它告诉Tornado应该用哪个类来响应请求）
    '''
    参数handlers：一个元组组成的列表，其中每个元组的第一个元素是一个用于匹配的正则表达式，第二个元素是一个RequestHanlder类
    Tornado在元组中使用正则表达式来匹配HTTP请求的路径（这个路径是URL中主机名后面的部分，不包括查询字符串和碎片）Tornado把这些正则表达式看作已经包含了行开始和结束锚点（即，字符串"/"被看作为"^/$"）
    '''
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])

    #app转为server（Application对象被传递给Tornado的HTTPServer对象）
    http_server = tornado.httpserver.HTTPServer(app)

    #设置server监听端口
    http_server.listen(options.port)

    #启动server（创建Tornado的IOLoop的实例）
    tornado.ioloop.IOLoop.instance().start()


"""
curl http://127.0.0.1:8000/?greeting=defias
curl -d foo=bar http://localhost:8000/
"""




