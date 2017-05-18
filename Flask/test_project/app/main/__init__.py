#coding=utf8
from flask import Blueprint

#解决问题：转换成程序工厂函数的操作让定义路由变复杂了。在单脚本程序中，程序实例存在于全局作用域中，路由可以直接使用app.route修饰器定义。但现在程序在运行时
#创建，只有调用create_app()之后才能使用app.route修饰器，这时定义路由就太晚了

#解决方法：Flask使用蓝本提供了更好的解决方法。蓝本和程序类似，也可以定义路由。不同的是，在蓝本中定义的路由处于休眠状态，直到蓝本注册到程序上后，路由才真正
#成为程序的一部分

#蓝本
main = Blueprint('main', __name__)  #参数：蓝本的名字和蓝本所在的包或模块

from . import views, errors
'''
导入这两个模块就能把路由和错误处理程序与蓝本关联起来
在脚本的末尾导入，这是为了避免循环导入依赖，因为在views.py和errors.py中还要导入蓝本main
'''