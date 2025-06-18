"""
name: 3065_超过阈值的最少操作数1.py
create_time: 2025/6/18 23:56
author: Ethan

Description: https://leetcode.cn/problems/minimum-operations-to-exceed-threshold-value-i/description/
"""
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return len([num for num in nums if num < k])


