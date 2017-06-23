#coding=utf8
import threading, multiprocessing
import time

'''
def loop():
    x = 0
    while True:
        x = x ^ 1

for i in range(multiprocessing.cpu_count()):  #multiprocessing.cpu_count(): CPU个数
    t = threading.Thread(target=loop)
    t.start()
'''

class MyThread(threading.Thread):
    def __init__(self,idd):
        threading.Thread.__init__(self)
        print idd

    def run(self):
        time.sleep(5)
        print "This is " + self.getName()

# class MyThread2(threading.Thread):
#     def __init__(self,idd):
#         threading.Thread.__init__(self)
#         print idd

#     def run(self):
#         time.sleep(8)



if __name__ == "__main__":
    t1=MyThread(999)
    #t2=MyThread2(998)
    t1.setDaemon(True)   #setDaemon的默认值是False
    t1.start()
    #t2.start()
    print "I am the father thread."


'''
对于普通线程，如果线程的任务没有结束，主线程不会退出，整个程序也不会退出
对于守护线程，即使线程任务还没有结束，如果主线程退出该线程也会退出；
'''
