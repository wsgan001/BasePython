#coding=utf8
#被测程序
import random

#不需要在代码中用import导入模块memory_profiler

@profile
def random_sort2(n):
    l = [random.random() for i in range(n)]
    l.sort()
    return l

if __name__ == "__main__":
    random_sort2(2000000)


#如果想知道每个函数和方法消耗了多少时间，以及这些函数被调用了多少次，可以使用cProfile模块
#python -m cProfile -s cumulative timing_functions.py   -s选项（累加）最终结果会根据每个函数的累计执行时间排序
