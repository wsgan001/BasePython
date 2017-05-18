#coding=utf8
from django.db import models

# Create your models here.

#模型类（对应数据库表，表名组成结构为：app名_类名，如：TestModel_test）
class Test(models.Model):
    name = models.CharField(max_length=20)  #对应数据库表字段  数据类型CharField相当于varchar
    #没有给表设置主键，但是Django会自动添加一个id作为主键
