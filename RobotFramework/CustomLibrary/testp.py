#coding=utf8
'''
created by defias
'''
#使用方法：
#本地自定义关键字库，将库目录（CustomLibrarty模块 包含__init__.py文件）置于python的模块目录/Library/Python/2.7/site-packages下，然后ride中导入即可使用

__version__ = '0.1'
from robot.api import logger

class Quntest(object):
    def runtest(self):   #方法就是robotframework中可以使用的关键字
        u'''
        this is a test
	'''
	print 'this is a testing'
	logger.debug("debug: xxxx")

    def runtest2(self):   #方法就是robotframework中可以使用的关键字
        u'''
        this is a test2
        '''
        import time
        print 'this is a testing2'
        print time.time()
        logger.debug("debug: xxxx")

    def _siyou(self):   #_开头的私有方法会被自动过滤掉
        print 'siyou'

    def testt3(self, *args):  #LIST型参数
        self._siyou()
        print args

    def testt4(self, **args):  #DICTIONARY型参数
        print args

    def testt5(self):
        yuno = yun2()
        return yuno    #返回对象



class yun2(object):
    def __init__(self, arg = 1):
        self.arg = arg

    def ppp(self):
        print self.arg


if __name__ == '__main__':
    Runtest().runtest()

