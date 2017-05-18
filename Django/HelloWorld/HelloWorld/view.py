#coding=utf8
from django.http import HttpResponse
from django.shortcuts import render

#视图函数
def hello(request):
    #return HttpResponse("Hello world! ! ")
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)  #渲染模板
