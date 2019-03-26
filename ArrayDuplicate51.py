#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
# @project: algorithm-python
# @Time : 2019/3/26 11:13 
# @Author : Lemon
# @File : ArrayDuplicate51.py
'''
题目描述
在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不
知道每个数字重复几次。请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应
输出是第一个重复的数字2。
解题思路：
解法一：用hash存储数据，key为数组数据，默认value值是0，如果出现了就修改为1。时间复杂度O(n),空间复杂度O(n)
解法二:时间复杂度O(n),空间复杂度O(1)(但是有比较大的数就比较吃亏)
    如果这个数组中没有重复的数字，那么排好序之后数字i将出现在i位置。遍历数组，当扫描到下标
i的数字时，用一个变量temp临时存取数字，对比是不是等于i。
    如果 array[i] == i,遍历下一个
    否则:
        如果：array[array[i]] == array[i]，找到重复的数字
        否则：array[array[i]]与array[i]进行交换
解题所获：
    python 中的for 如果对象时列表的话，会自动叠加value值，java中的数组for循环一般叠加的是数组下标key值，而且可以
控制是否加一,本题因为要控制for的下标，所以不能用for,只能用while来替代
    python 中未初始化的数组不能直接duplication[0] = 1,只能duplication.append(1)
    python 中关于两数进行交换直接a, b = b, a 不需要另外设置变量，但是不能这么写
        numbers[numbers[i]], numbers[i] = numbers[i]，numbers[numbers[i]] 因为这个过程中numbers[i]变化了，所以
        会出bug
'''


class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        i = 0
        while i < len(numbers):
            if numbers[i] == i:
                i += 1
            else:
                if numbers[i] == numbers[numbers[i]]:
                    duplication.append(numbers[i])
                    return True
                else:
                    a, b = numbers[numbers[i]], numbers[i]
                    numbers[numbers[i]], numbers[i] = b, a
        return False


if __name__ == "__main__":
    test = [2, 1, 3, 1, 4]
    result = []
    isTrue = Solution().duplicate(numbers=test, duplication=result)
    print(isTrue)
    print(result)
