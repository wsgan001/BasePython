#coding=utf8
from fabric.api import *


env.user = 'root'
env.hosts = ['192.168.3.3',]
env.password = 'tataufo'



def remote_task():
    with cd('/home'):   #with上下文管理器，让后面执行的语句继承当前状态
        run('ls -l')
