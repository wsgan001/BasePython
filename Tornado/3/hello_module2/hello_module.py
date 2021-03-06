#coding=utf8
import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
import os.path

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)


class RecommendedHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            "recommended.html",
            page_title="Burt's Books | Recommended Reading",
            header_text="Recommended Reading",
            books=[
                {
                    "title":"Programming Collective Intelligence",
                    "subtitle": "Building Smart Web 2.0 Applications",
                    "image":"/static/images/collective_intelligence.jpg",
                    "author": "Toby Segaran",
                    "date_added":1310248056,
                    "date_released": "August 2007",
                    "isbn":"978-0-596-52932-1",
                    "description":"<p>This fascinating book demonstrates how you "
                        "can build web applications to mine the enormous amount of data created by people "
                        "on the Internet. With the sophisticated algorithms in this book, you can write "
                        "smart programs to access interesting datasets from other web sites, collect data "
                        "from users of your own applications, and analyze and understand the data once "
                        "you've found it.</p>"
                },

                {
                    "title":"Programming Collective Intelligence2",
                    "subtitle": "Building Smart Web 2.0 Applications",
                    "image":"/static/images/collective_intelligence.jpg",
                    "author": "Toby Segaran",
                    "date_added":1310248056,
                    "date_released": "August 2007",
                    "isbn":"978-0-596-52932-1",
                    "description":"<p>This fascinating book demonstrates how you "
                        "can build web applications to mine the enormous amount of data created by people "
                        "on the Internet. With the sophisticated algorithms in this book, you can write "
                        "smart programs to access interesting datasets from other web sites, collect data "
                        "from users of your own applications, and analyze and understand the data once "
                        "you've found it. 111111111111111111111111111111111111111</p>"
                },
            ]
        )

class BookModule(tornado.web.UIModule): #模块
    def render(self, book):
        return self.render_string('modules/book.html', book=book) #让模块指向一个模板文件而不是在模块类中直接渲染字符串

    # def html_body(self):
    #     return "<div class=\"addition\"><p>html_body()</p></div>"


    #Tornado允许使用embedded_css和embedded_javascript方法嵌入其他的CSS和JavaScript文件
    # def embedded_javascript(self):
    #     return "document.write(\"<p>embedded_javascript()</p>\")"

    # def embedded_css(self):
    #     return ".addition {color: #A1CAF1}"

    #可以使用javascript_files()和css_files()来包含完整的文件，不论是本地的还是外部的
    # def css_files(self):
    #     return "/static/css/sample.css"

    # def javascript_files(self):
    #     return "/static/js/sample.js"


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r'/', RecommendedHandler)],
        template_path=os.path.join(os.path.dirname(__file__), 'templates'),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        ui_modules={'Book': BookModule},
        debug=True,
    )
    server = tornado.httpserver.HTTPServer(app)
    server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
