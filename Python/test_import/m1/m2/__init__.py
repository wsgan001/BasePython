#coding=utf8
#包：m2


def www():
    print 'www'


from . import sdf3      #或：__all__ = ['sdf3', 'www']

