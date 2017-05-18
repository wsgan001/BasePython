#coding=utf8
#复杂示例
import os.path
import random
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class MungedPageHandler(tornado.web.RequestHandler):
    def map_by_first_letter(self, text):
        mapped = dict()
        for line in text.split('\r\n'):
            for word in [x for x in line.split(' ') if len(x) > 0]:
                if word[0] not in mapped: mapped[word[0]] = []
                mapped[word[0]].append(word)
        return mapped

    def post(self):
        source_text = self.get_argument('source')
        text_to_change = self.get_argument('change')
        source_map = self.map_by_first_letter(source_text)  #将传入的文本（从source域）分割成单词，然后创建一个字典，其中每个字母表中的字母对应文本中所有以其开头的单词
        change_lines = text_to_change.split('\r\n')
        print 'source_map:', source_map
        print 'change_lines:', change_lines
        self.render('munged.html', source_map=source_map, change_lines=change_lines,
                choice=random.choice) #Python标准库的random.choice函数以一个列表作为输入，返回列表中的任一元素

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r'/', IndexHandler),
                  (r'/poem', MungedPageHandler),
                  ],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),  #指定了应用程序放置静态资源（如图像、CSS文件、JavaScript文件等）的目录

        #它调用了一个便利的测试模式：tornado.autoreload模块，此时，一旦主要的Python文件被修改，Tornado将会尝试重启服务器，并且在模板改变时会进行刷新。对于快速改变和实时更新这非常棒，但不要再生产上使用它，因为它将防止Tornado缓存模板
        debug=True

    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


