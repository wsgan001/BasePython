#coding=utf8
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from mysite.views import hello, current_datetime, hours_ahead

# urlpatterns = [
#     url(r'^admin/', include(admin.site.urls)),
# ]

#URLconf就是URL模式以及要为该URL模式调用的视图函数之间的映射表
urlpatterns = patterns('',
    (r'^hello/$', hello),  #URLpattern 元组中第一个元素是模式匹配字符串（正则表达式）；第二个元素是那个模式将使用的视图函数
    (r'^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead), #动态URL(将匹配类似 /time/plus/2/ , /time/plus/25/  最大允许99)
                                              #使用圆括号把参数在URL模式里标识出来(传递到视图函数里去)
)
