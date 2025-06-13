"""
name: 1365_有多少小于当前数字的数字.py
create_time: 2025/6/13 23:42
author: Ethan

Description: https://leetcode.cn/problems/how-many-numbers-are-smaller-than-the-current-number/
"""
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums, reverse=True)
        len_nums = len(nums)
        res = []
        for i in range(len_nums):
            for j in range(len_nums):
                if sorted_nums[j] < nums[i]:
                    res.append(len_nums - j)
                    break
                # 如果到最后还是没有找到比它小的数，那么就是0
                if j == len_nums - 1:
                    res.append(0)

        return res

