#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
# @project: algorithm-python
# @Time : 2019/4/27 9:56 
# @Author : Lemon
# @File : SortQuickSortByLemonLin.py
"""
 * 快速排序算法是对冒泡排序的一种改进，其基本思想是基于分治法，在待排序的N个元素中任取一个元素pivot
 * 作为基准，通过一趟排序将待排序表划分为独立的两部分L[1...k-1] 和L[k+1...n],使得L[1...k-1]中所有元素小于
 * pivot,L[k+1...n]中所有的元素大于pivot，则基准元素放在了其最终位置L(k)上，这个过程称为一趟快速排序。
 * 而后分别递归地对两个子表重复上述过程，直至每部分内只有一个元素或空为止，即所有元素放在了其最终位置上。
 *
 * 快速排序提出至今，有许多不同的划分操作版本，笔者写的是假设每次总是以当前表中第一个元素作为枢纽值（基准）
 * 对表进行划分。
 *
 * 空间效率：由于快速排序是递归的，需要借助一个递归工作栈来保存每一层递归调用的必要信息，其容量应与
 * 递归调用的最大深度一致。最好情况下为log2(n+1),最坏情况下，因为要进行n-1次递归调用，所以栈的深度为
 * O(n).平均情况下，栈的深度为O（log2(n)）
 *
 * 时间效率：快速排序的运行时间与划分是否堆成有关，最坏情况发生在两个区域分别包含n-1 个元素和0 个元素，这种
 * 最大程度的不对称若发生在每一层递归上，即对应于初始排序表基本有序或基本逆序，就得到最坏时间复杂度O(n2)
 *
 * 平均情况下O(nlog2n),快速排序是所有排序算法中平均性能最优的排序算法。
 *
 * 稳定性：划分算法中，若右端区间存在两个关键字相同，且均小于基准值得记录，则在交换到左端区间后，它们
 * 的相对位置会发生变化，即快排是个不稳定的排序方法
"""


class Solution:
    def SortQuickSort(self, arr, low, high):
        lo = low
        h = high
        if lo < h:
            temp = arr[lo]
            while lo < h:
                while lo < h and temp < arr[h]:
                    h -= 1
                if lo < h:
                    arr[lo] = arr[h]
                    lo += 1
                while lo < h and temp > arr[lo]:
                    lo += 1
                if lo < h:
                    arr[h] = arr[lo]
                    h -= 1
            arr[lo] = temp
        if lo <= h:
            self.SortQuickSort(arr, low, lo-1)
            self.SortQuickSort(arr, lo+1, high)
        return arr


if __name__ == "__main__":
    test = [0, 3, 2, 6, 4]
    result = Solution().SortQuickSort(test, 0, 4)
    print(result)
