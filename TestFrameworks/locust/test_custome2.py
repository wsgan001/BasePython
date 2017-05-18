#coding=utf8
from locust import Locust, events, task, TaskSet
import socket
import time
import struct

class TCPClient(object):
    '''
    TCP Client
    '''
    def __init__(self, host, port):
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect((host, port))
        except (socket.error, socket.herror) as e:
            print "Connect is error, Exception is %s" % str(e)
            sys.exit()
        except socket.timeout as e:
            print "Socket timeout, Exception is %s" % str(e)
            sys.exit()

    def TCPRequest(self, data, recnlen=100):
        try:
            self.s.sendall(data)
            response = self.s.recv(recnlen)
        except Exception as e:
            print "send Exception is %s" % str(e)
            raise
        return response


class TCPLocustClient(TCPClient):
    def __getattr__(self, name):
        func = TCPClient.__getattr__(self, name)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                total_time = int((time.time() - start_time) * 1000)
                events.request_failure.fire(request_type="tcp", name=name, response_time=total_time, exception=e)
            else:
                total_time = int((time.time() - start_time) * 1000)
                events.request_success.fire(request_type="tcp", name=name, response_time=total_time, response_length=0)
        return wrapper


class TCPLocust(Locust):
    def __init__(self, *args, **kwargs):
        super(TCPLocust, self).__init__(*args, **kwargs)
        self.client = TCPLocustClient(self.host, self.port)


class mytest(TaskSet):
    @task(weight=1)
    def transaction_1(self):
        #data = "111111111111\r\n"
        data = struct.pack("!2sHi","go",0,0)
        response = self.client.TCPRequest(data)
        print response

    #断言
    #如何关闭连接？


class ApiUser(TCPLocust):
    task_set = mytest
    host = '192.168.1.176'
    port = '59001'
    min_wait = 5000
    max_wait = 5000










