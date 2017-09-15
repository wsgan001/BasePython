#coding=utf8
import sys

if len(sys.argv)<6:
    print 'count of argv less 6!'
    exit()
host = sys.argv[1]
port_online = int(sys.argv[2])
uid = sys.argv[3]
sn = sys.argv[4]
iccid = sys.argv[5]
print host, port_online, uid, sn, iccid
