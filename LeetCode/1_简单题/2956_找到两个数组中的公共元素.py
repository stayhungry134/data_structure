"""
name: 2956_找到两个数组中的公共元素.py
create_time: 2025/6/25 0:57
author: Ethan

Description: https://leetcode.cn/problems/find-common-elements-between-two-arrays/description/
"""
from typing import List


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # set 也是属于哈希表实现，它只有键，没有值，操作更快
        s1 = set(nums1)
        s2 = set(nums2)
        a1 = 0
        a2 = 0
        for num1 in nums1:
            if num1 in s2:
                a1 += 1
        for num2 in nums2:
            if num2 in s1:
                a2 += 1
        return [a1, a2]
