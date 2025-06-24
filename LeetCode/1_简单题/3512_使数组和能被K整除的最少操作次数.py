"""
name: 3512_使数组和能被K整除的最少操作次数.py
create_time: 2025/6/24 23:58
author: Ethan

Description: https://leetcode.cn/problems/minimum-operations-to-make-array-sum-divisible-by-k/description/
"""
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) % k