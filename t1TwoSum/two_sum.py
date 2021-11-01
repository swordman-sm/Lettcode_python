#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element
twice.
<p>
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]
<p>
在数组中找到 2 个数之和等于给定值的数字，结果返回 2 个数字在数组中的下标。
"""


def twoSum(nums: list[int], target: int) -> list[int]:
    # 使用hash存储, 查询时间复杂度O(1)
    temp_dic = {}
    for i in range(len(nums)):
        # 1.找到和为target的另一个数的值
        pair = target - nums[i]
        # 2.map中查询pair的索引是否存在
        if pair in temp_dic:
            return [i, temp_dic[pair]]
        # 3.map中找不到pair则将当前数字与索引放入map以便下次查询
        temp_dic[nums[i]] = i
