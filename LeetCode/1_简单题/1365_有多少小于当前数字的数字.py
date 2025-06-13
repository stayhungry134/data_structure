"""
name: 1365_有多少小于当前数字的数字.py
create_time: 2025/6/13 23:42
author: Ethan

Description: https://leetcode.cn/problems/how-many-numbers-are-smaller-than-the-current-number/
"""
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            cnt = 0
            for j in range(len(nums)):
                if j != i and nums[j] < nums[i]:
                    cnt += 1
            res.append(cnt)

        return res
