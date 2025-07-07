"""
name: 3002_移除后集合的最多元素数.py
create_time: 2025/7/4 23:55
author: Ethan

Description: https://leetcode.cn/problems/maximum-size-of-a-set-after-removals/
"""
from typing import List


class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        set1 = set(nums1)
        set2 = set(nums2)
        set_all = set(nums1 + nums2)

        res1 =  min(n // 2, len(set1)) + min(n // 2, len(set2))
        return min(res1, len(set_all))

num1 = [1,2,3,4,5,6]
num2 = [2,3,2,3,2,3]

print(Solution().maximumSetSize(num1, num2))