#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
# @project: algorithm-python
# @Time : 2019/3/26 20:37 
# @Author : Lemon
# @File : ArrayFindInPartiallySortedMatrix03.py
'''
 题目描述
 * 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都
 * 按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中
 * 是否含有该整数
 解题思路：
    从右上角开始比较，设要查找的数是target
    if（target == 右上角的数）
        :return true
    elif(target < 右上角的数)
        去掉右上角的数所在的列
        continue
    elif(target > 右上角的数)
        去掉右上角的数所在的行
        continue
'''


class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        i = 0  # 右上角的数的行号
        j = len(array[0])-1  # 右上角的数的列号
        while i < len(array) and j >= 0:
            if target == array[i][j]:
                return True
            elif target < array[i][j]:
                j -= 1
                continue
            elif target > array[i][j]:
                i += 1
                continue
        return False


if __name__ == "__main__":
    array = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
    result = Solution().Find(12, array)
    print(result)
