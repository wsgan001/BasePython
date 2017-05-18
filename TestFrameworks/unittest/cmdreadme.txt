命令行
从命令行中可以运行单元测试的模块，类，甚至单独的测试方法。
python -m unittest test_module1 test_module2  #同时测试多个module
python -m unittest test_module.TestClass
python -m unittest test_module.TestClass.test_method

显示更详细的测试结果的说明使用-vflag：
python -m unittest -v test_module

查看所有的命令行选项使用命令:
python -m unittest -h




跳过测试和预期的失败
Unittest支持跳过单个的测试方法甚至整个类的测试。使用 skip() decorator来设置特定跳过的条件，如指定操作系统不执行该测试。

@unittest.skipIf(mylib.__version__ < (1, 3), "not supported in this library version")
def test_format(self):
    # Tests that work for only a certain version of the library.
    pass
执行的时候如果满足跳过条件，控制台会将后面的说明打印出来，并跳过该测试用例。跳过类也是相似的写法。
也可以自定义skipping装饰器。
定义预期的失败使用unittest.expectedFailure(),运行时 ,如果测试失败,测试不算作失败。
