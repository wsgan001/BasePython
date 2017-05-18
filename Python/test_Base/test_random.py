#coding=utf8
import os
import string
import random

# print ''.join(map(lambda xx:(hex(ord(xx))[2:]),os.urandom(16)))


print ''.join([(string.ascii_letters+string.digits)[x] for x in random.sample(range(0,62),11)])


#随机电话号码
print '158' + ''.join([str(random.randint(0, 9)) for x in range(0,8)])
