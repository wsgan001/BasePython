#coding=utf8
import os

#python与shell之间

var = 'test'
os.environ['var_shell'] = var
print os.system('echo $var_shell')


"""
要注意的是:
1、通过环境变量进行参数传递只能传递字符型变量
2、利用环境变量进行参数传递存在一个很大的问题。对于单线程的任务而言这个问题不存在，但是当涉及多线程时，需要慎用。由于环境变量是整个工作环境共享，在某
一时刻环境变量的值是一个值，如果在不同的线程中改变同一个环境变量的值的话，该环境变量保持最后一次被赋值的结果
"""
