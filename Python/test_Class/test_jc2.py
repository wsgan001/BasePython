#coding=utf8

class test1(object):
    a1 = '123'
    def __init__(self, v):  #__init__会被子类继承
        self.value1 = v

    def ppp(self):
        print self.value1

class test2(test1):
    pass

O2 = test2('xxx')
print O2.a1
print O2.value1
O2.ppp()
print dir(O2)
print '-----------\n'

class test3(test1):
    def __init__(self, v):
        super(test3, self).__init__(v)
        self.value2 = v + '---'
        self.p1()

    def ppp(self, p):
        super(test3, self).ppp()
        print self.value1 + "+++" + p
        print self.value2 + "+++" + p

    def p1(self):
        print 'p1'

O3 = test3('www')
O3.ppp('111')



