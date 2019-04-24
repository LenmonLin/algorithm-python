#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
# @project: algorithm-python
# @Time : 2019/4/24 20:45 
# @Author : Lemon
# @File : ArrayGetNumberOfK38.py
"""
*题目描述
 * 统计一个数字在排序数组中出现的次数。
 *
 * 解题思路：
 * 基本思路是使用hashmap中的key来记录array中的数，使用value来记录出现的次数。
 * 不能用数组的原因是，如果数字很大，array={300},那么要申请一个300大小的数组，非常的浪费。

 两轮循环，第一轮，先放入字典，key为数字，value为0。（初始化）
 第二轮，对value 进行计数。
"""

class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if data is None:
            return 0
        dist = {}
        # 加入flag 的目的是判断当k值不等于key时，需要返回0
        flag = False
        for i in data:
            if i == k:
                flag = True
            dist[i] = 0
        # 先取出value值，再加一放入
        for i in data:
            value = dist[i]
            dist[i] = value+1
        if flag is False:
            return 0
        return dist[k]


if __name__ == "__main__":
    test = [1, 2, 3, 3, 4]
    result = Solution().GetNumberOfK(test, 5)
    print(result)
