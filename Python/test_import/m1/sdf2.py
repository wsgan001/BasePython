#coding=utf8

#或：
#import sys
#sys.path.append("m2")

##导入一个包时，实际上是导入了它的__init__.py文件
from m2 import * #或：from m2 import www,sdf3

www()

sdf3.test_sdf3()


def test_sdf2():
    print 'test_sdf2'
