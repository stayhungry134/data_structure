"""
name: 496_下一个更大元素1.py
create_time: 2025/6/23 23:53
author: Ethan

Description: https://leetcode.cn/problems/next-greater-element-i/
"""
from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        tem_map = {num: i for i, num in enumerate(nums2)}
        res = []
        for num in nums1:
            i = tem_map[num]
            res.append(-1)
            for j, num2 in enumerate(nums2[i:]):
                if num2 > num:
                    res.pop()
                    res.append(num2)
                    break
        return res
