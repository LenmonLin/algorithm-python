#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
# @project: algorithm-python
# @Time : 2019/4/25 19:39 
# @Author : Lemon
# @File : ArrayIsContinuous44.py
"""
* 题目：扑克牌顺子
 *
 * 题目：随机抽取扑克牌中的5张牌，判断是不是顺子，即这5张牌是不是连续的。
 * 其中A看成1，J看成11，Q看成12，K看成13，大小王可以看成任何需要的数字。
 *
 * 解题思路：
 * 其实就是判断取出的数是不是连续数组；
 * 步骤：
 * 1、对取出的数据进行排序：用Arrays.sort
 * 2、计算数据中包含的0的个数，0的个数可以替换非顺序的空白
 * 3、计算排好序的相邻数据之间的空缺总数，和2对比，0总数多，就算连续数组，否则不算
 * 4、注意异常情况，如果有非0数字重复出现，则该数组不是连续的，即有对子不能为顺子
"""


class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if numbers is None or len(numbers) == 0:
            return False
        numbers = sorted(numbers)
        zeroOfNumbers = 0
        blankOfNumbers = 0
        for i in range(0, len(numbers)):
            if numbers[i] == 0:
                zeroOfNumbers += 1
            if i != len(numbers)-1 and numbers[i] != 0:
                blankOfNumbers += numbers[i+1]-numbers[i]-1
                # 如果有对子的话，就不是连续数组
                if numbers[i+1] == numbers[i]:
                    return False
        if zeroOfNumbers < blankOfNumbers:
            return False
        return True


if __name__ == "__main__":
    test = [0, 3, 2, 6, 4]
    result = Solution().IsContinuous(test)
    print(result)


