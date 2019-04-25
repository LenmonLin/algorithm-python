#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
# @project: algorithm-python
# @Time : 2019/4/25 11:09 
# @Author : Lemon
# @File : ArrayGreatestSumOfSubarrays31.py
"""
 *题目描述
 * HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。今天测试组开完会后,他又发话了:在古老的一维模式
 * 识别中,常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。但是,如果向量中包含负数,
 * 是否应该包含某个负数,并期望旁边的正数会弥补它呢？例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从
 * 第0个开始,到第3个为止)。给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至
 * 少是1)
 *
 * 解题思路：
 * 基本思想用在线法处理，设置两个变量来记录，currentSum记录在线过程中是否累加和大于0，
 * 如果大于0就继续累加，如果小于0就舍弃；
 * GreatSum用于记录最大的值,过程中和currentSum比较
 *
 * 要点二：
    注意GreatSum不能设置为0，应该设置成一个极小的数，否则如果都是数组都是负数的话，
    就返回0，这个是有问题的.
    修正方案：可以把array[0] 赋值给GreatSum
"""


class Solution:

    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if array is None:
            return 0
        currentSum = 0
        GreatSum = array[0]
        for i in array:
            if currentSum < 0:
                currentSum = i
            else:
                currentSum += i
            if currentSum > GreatSum:
                GreatSum = currentSum
        return GreatSum


if __name__ == "__main__":
    test = [6, -3, -2, 7, -15, 1, 2, 2]
    result = Solution().FindGreatestSumOfSubArray(test)
    print(result)
