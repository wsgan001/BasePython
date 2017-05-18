#coding=utf8

#无参数装饰器 – 包装无参数函数
def decorator(func):
    print "hello"
    return func

@decorator
def foo():
    pass

foo()
print '\n---------------------\n'


#无参数装饰器 – 包装带参数函数
def decorator_func_args(func):
    def handle_args(*args, **kwargs): #处理传入函数的参数
        print "begin"
        func(*args, **kwargs)   #函数调用
        print "end"
    return handle_args


@decorator_func_args
def foo2(a, b=2):
    print a, b

foo2(1)
print '\n---------------------\n'


#带参数装饰器 – 包装无参数函数
def decorator_with_params(arg_of_decorator):#这里是装饰器的参数
    print arg_of_decorator
    #最终被返回的函数
    def newDecorator(func):
        print func
        return func
    return newDecorator


@decorator_with_params("deco_args")
def foo3():
    pass
foo3()
print '\n---------------------\n'


#带参数装饰器– 包装带参数函数
def decorator_whith_params_and_func_args(arg_of_decorator):
    def handle_func(func):
        def handle_args(*args, **kwargs):
            print "begin"
            func(*args, **kwargs)
            print "end"
            print arg_of_decorator, func, args,kwargs
        return handle_args
    return handle_func


@decorator_whith_params_and_func_args("123")
def foo4(a, b=2):
    print "Content"

foo4(1, b=3)
















