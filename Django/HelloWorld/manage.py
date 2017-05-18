#!/usr/bin/env python
#coding=utf8
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HelloWorld.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


"""
启动：python manage.py runserver
项目中如果代码有改动，服务器会自动监测代码的改动并自动重新载入，所以如果已经启动了服务器则不需手动重启


python manage.py startapp TestModel
创建一个TestModel的app（Django规定，如果要使用模型必须要创建一个app）


python manage.py syncdb
创建数据表

"""
