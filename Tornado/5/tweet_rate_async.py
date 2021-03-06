#coding=utf8
#版本2：带有回调函数的Tornado异步HTTP客户端

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient
import urllib
import json
import datetime
import time
from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous   #异步装饰器告诉Tornado保持连接开启 当使用@tornado.web.asynchonous装饰器时，Tornado永远不会自己关闭连接。必须在你的RequestHandler对象中调用finish方法来显式地告诉Tornado关闭连接
    def get(self):
        query = self.get_argument('q')
        client = tornado.httpclient.AsyncHTTPClient()  #AsyncHTTPClient的fetch方法并不返回调用的结果。取而代之的是它指定了一个callback参数；指定的方法或函数将在HTTP请求完成时被调用，并使用HTTPResponse作为其参数
        client.fetch("http://search.twitter.com/search.json?" + \
                urllib.urlencode({"q": query, "result_type": "recent", "rpp": 100}),
                callback=self.on_response)
        #在通常情况下Tornado默认在函数处理返回时关闭客户端的连接，但是当处理一个需要回调函数的异步请求时，需要连接保持开启状态直到回调函数执行完毕

    def on_response(self, response):
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
</div>""" % (self.get_argument('q'), tweets_per_second))
        self.finish()  #回调方法结尾处调用self.finish()来关闭连接（否则，请求将可能挂起，浏览器可能不会显示我们已经发送给客户端的数据）

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
