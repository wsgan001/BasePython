#coding=utf8

from django.http import HttpResponse, Http404
import datetime

#视图函数
def hello(request):  #每个视图函数至少要有一个参数request
    return HttpResponse("Hello world") #返回一个HttpResponse对象



def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def hours_ahead(request, offset):  #offset参数是从匹配的URL里提取出来的（任意命名它，如果请求URL是/time/plus/3/，那么offset将会是3，捕获值永远都是字符串类型，严格来说是Unicode objects）
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    assert False
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
