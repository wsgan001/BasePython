#coding=utf8
#版本3：使用生成器模式的异步请求 （性能同版本2）
#避免写回调函数（可能出现调用一个回调函数的回调函数的回调函数...）， 使得开发起来更加符合正常逻辑思维

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient
import tornado.gen  #Tornado 2.1版本引入了tornado.gen模块，可以提供一个更整洁的方式来执行异步请求
import urllib
import json
import datetime
import time
from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine  #@tornado.gen.engine装饰器的使用需要刚好在get方法的定义之前；这将提醒Tornado这个方法将使用tornado.gen.Task类
    def get(self):       #在tornado3发布之后，强化了coroutine的概念，在异步编程中，替代了原来的gen.engine， 变成现在的gen.coroutine
        query = self.get_argument('q')
        client = tornado.httpclient.AsyncHTTPClient()

        #请求处理程序中返回HTTP响应，而不是回调函数中。因此，代码更易理解，而HTTP请求依然是异步执行的
        response = yield tornado.gen.Task(client.fetch,   #yield的使用返回程序对Tornado的控制，允许在HTTP请求进行中执行其他任务
                "http://search.twitter.com/search.json?" + \
                urllib.urlencode({"q": query, "result_type": "recent", "rpp": 100}))
        body = json.loads(response.body)
        result_count = len(body['results'])
        now = datetime.datetime.utcnow()
        raw_oldest_tweet_at = body['results'][-1]['created_at']
        oldest_tweet_at = datetime.datetime.strptime(raw_oldest_tweet_at,
                "%a, %d %b %Y %H:%M:%S +0000")
        seconds_diff = time.mktime(now.timetuple()) - \
                time.mktime(oldest_tweet_at.timetuple())
        tweets_per_second = float(result_count) / seconds_diff
        self.write("""
<div style="text-align: center">
    <div style="font-size: 72px">%s</div>
    <div style="font-size: 144px">%.02f</div>
    <div style="font-size: 24px">tweets per second</div>
</div>""" % (query, tweets_per_second))
        self.finish()

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
