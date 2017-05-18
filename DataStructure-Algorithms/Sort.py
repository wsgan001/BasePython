#coding=utf8

def BubbleSort(L):
    '''
    冒泡排序： 一趟一趟的比较相邻的元素
    '''
    n = len(L)
    flag = True
    while flag and n>0:
        flag = False
        for i in xrange(1,n):  #比较多少趟
            for j in xrange(0,n-i):  #每一趟比较多少次
                if L[j] > L[j+1]:
                    flag = True
                    L[j], L[j+1] = L[j+1], L[j]

def SelectSort(L):
    '''
    选择排序： 找最（大/小）值
    '''
    n = len(L)
    for i in xrange(0,n):
        mii = i
        for j in xrange(i+1, n):
            if L[j] < L[mii]:
                mii = j
        if i != mii:
            L[mii], L[i] = L[i], L[mii]


def InsertSort(L):
    '''
    插入排序： 把数组第一个元素看成是已排好序的仅有一个元素的数组，然后逐步向已拍好序的一段中插入剩余元素到合适的位置上
    '''
    n = len(L)
    for i in xrange(1,n):
        tmp = L[i]
        j = i
        while j>0 and L[j-1] > tmp:
            L[j] = L[j-1]
            j = j-1
        L[j] = tmp



def shell_sort(a_list):
    '''
    希尔排序
    '''
    #how many sublists, also how many elements in a sublist
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        print("After increments of size", sublist_count, "The list is", a_list)
        sublist_count = sublist_count // 2

def gap_insertion_sort(a_list, start, gap):
    #start+gap is the second element in this sublist
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap] #move backward
            position = position - gap
            a_list[position] = current_value





#桶排序


#基数排序


#计数排序


if __name__ == '__main__':
    L = [23,34,57,3,2,3,86,45,6,9]
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    #print L
    #BubbleSort(L)
    #SelectSort(L)
    #InsertSort(L)
    #merge_sort(L)
    #quick_sort(a_list)
    shell_sort(a_list)
    print(a_list)
    #print L
