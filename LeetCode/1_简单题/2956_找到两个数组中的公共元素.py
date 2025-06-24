"""
name: 2956_找到两个数组中的公共元素.py
create_time: 2025/6/25 0:57
author: Ethan

Description: https://leetcode.cn/problems/find-common-elements-between-two-arrays/description/
"""
from typing import List


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        count_1 = Counter(nums1)
        count_2 = Counter(nums2)

        res = [0, 0]

        for num1 in count_1.keys():
            if num1 in count_2:
                res[0] += count_1[num1]
        for num2 in count_2.keys():
            if num2 in count_1:
                res[1] += count_2[num2]
        return res
