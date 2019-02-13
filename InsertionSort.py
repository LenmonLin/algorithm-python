#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Time    : 2019-02-13 17:41
# @Author  : Lemon
# @File    : InsertionSort.py


def insertionSort(list):
    for i in range(1 ,len(list)):
        tmp = list[i]

        # Python中没有for(i;i<length;i++)这种类似Java的循环
        j=i
        while j>0 and list[j-1]>tmp:
            # 有序数组是向右移动，所以是从前往后移动
            list[j]=list[j-1]
            j=j-1

        list[j] = tmp



if __name__ == "__main__":
    test = [10,2 ,4 ,5]
    insertionSort(test)
    print(test)