#coding=utf8
import socket
import struct

HOST = '192.168.1.176'
PORT = 59001

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)      #定义socket类型，网络通信，TCP
print s.__getattribute__('connect')

s.connect((HOST,PORT))       #要连接的IP与端口

runn = True

while runn:
    #cmd = raw_input("Please input cmd:")       #与人交互，输入命令
    sdata = struct.pack("!2sHi","go",0,0)
    s.sendall(sdata)      #把命令发送给对端
    data=s.recv(8)     #把接收的数据定义为变量
    print data         #输出变量
    runn = False

s.close()   #关闭连接
