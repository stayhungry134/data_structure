"""
name: 2465_不同的平均值数目.py
create_time: 2025/6/19 11:51
author: Ethan

Description: https://leetcode.cn/problems/number-of-distinct-averages/description/
"""
from typing import List


class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        res = set()
        sorted_nums = sorted(nums)

        for i in range(len(nums)//2):
            res.add((sorted_nums[i] + sorted_nums[-i - 1]))

        return len(res)
