#coding=utf8

#把10进制转整形换成16进制
print hex(88)   #'0x58'

#把浮点型转换成16进制
print 1.23.hex()   #'0x1.3ae147ae147aep+0'

#内置函数hex和binascii.hexlify()的区别就在于,hex只能接受整形不能接受字符串
#hex('88')

#把十进制整型转换成二进制
print bin(88)

#把十进制转换成八进制
print oct(500)


#把一个整形转换成ASCII码表中对应的单个字符
print chr(98)

#和chr相反，把ASCII码表中的字符转换成对应的整形
print ord('b')
