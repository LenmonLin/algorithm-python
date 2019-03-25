#! python3.7
# -*- coding: utf-8 -*-
# @project: algorithm-python
# @Time : 2019/3/22 11:34 
# @Author : Lemon
# @File : ArrayContinuesSquenceWithSum41_2.py
"""
题目描述
小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。但是他并
不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。没多久,他就得到另一组连
续正数和为100的序列:18,19,20,21,22。现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序
列? Good Luck!
输出描述:
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序

解题思路：分别用两个变量start，end记录cur_sum头部和尾部，同时cur_sum记录当前和。
当cur_sum小于目标和tsum时，end后移，当前相加的数变多，cur_sum增大；
当cur_sum大于目标和tsum时，start后移，当前相加的数变少，cur_sum减小；
主要，因为至少有两个数相加，所以start变量要小于middle=(tsum+1)/2,否则当start变量大于middle时，
至少两个相加的数都大于tsum/2，那么相加肯定大，start再后移也是大，没有效果了。
这里要解决寻找出所有的满足添加的序列，而不止一个序列,解决列表中套列表的问题。
"""


class Solution:
    def FindContinuousSequence(self, tsum):
        if tsum < 3:
            return []
        start = 1
        end = 2
        curSum = start + end
        middle = (tsum+1)/2
        sumList = [1, 2]
        resultList = []
        while start < middle:
            if curSum < tsum:
                end += 1
                curSum = curSum + end
                sumList.append(end)
            elif curSum > tsum:
                sumList.remove(start)
                curSum = curSum-start
                start += 1
            else:
                # 这里不能直接写resultList.append(sumList)，因为后序还要对sumList变动，变动
                # 之后resultList里面的值也变动了，所以需要一个函数重新添加列表
                self.AddContinuousSequence(start, end, resultList)
                # 当寻找到一个序列时，为了寻找下一个序列，需要先把start向后移动一位，重新寻找
                sumList.remove(start)
                curSum = curSum-start
                start += 1
        # 为了当不满足条件时，返回空数组,同时解决列表中套列表的问题
        return resultList

    def AddContinuousSequence(self, start, end, resultList):
        newList = []
        # 注意这里要end要加一
        for start in range(start, end+1):
            newList.append(start)
        resultList.append(newList)


if __name__ == "__main__":
    result = Solution().FindContinuousSequence(9)
    print(result)
