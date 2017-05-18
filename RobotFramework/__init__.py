#coding=utf8
from testp import Quntest

__version__ = '0.1'
class CustomLibrary(Quntest):
	"""
		这里也可以装x的写上我们创建的CustomLibrary如何如何
	"""
	ROBOT_LIBRARY_SCOPE = 'GLOBAL'   #作用域： TEST CASE     TEST SUITE   GLOBAL
