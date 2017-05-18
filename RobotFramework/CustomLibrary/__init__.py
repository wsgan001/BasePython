#coding=utf8
from testp import Quntest

__version__ = '0.1'
class CustomLibrary(Quntest):
	"""
		这里也可以装x的写上我们创建的CustomLibrary如何如何
	"""
	ROBOT_LIBRARY_SCOPE = 'GLOBAL'   #作用域： TEST CASE     TEST SUITE   GLOBAL
    ROBOT_LIBRARY_VERSION = 0.1   #测试库版本号   不设置时会尝试读取"__version__"属性
    #ROBOT_LIBRARY_DOC_FORMAT = 'reST'   #文档格式： ROBOT HTML TEXT reST
