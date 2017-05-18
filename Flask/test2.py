#coding=utf8

from hello import app
from flask import current_app
#print current_app.name

app_ctx = app.app_context()  #获得程序上下文
app_ctx.push()  #激活程序上下文
print current_app.name

app_ctx.pop()


#上下文全局变量：
#current_app   当前激活程序的程序实例 （程序上下文）
#g   处理请求时用作临时存储的对象，每次请求都会重设这个变量（程序上下文）
#request   请求对象，封装了http请求中的内容 （请求上下文）
#session  用户会话，用于存储请求之间需要“记住”的值得字典 （请求上下文）


#url映射：url和视图函数之间的对应关系
print app.url_map
