"""
name: 1720_解码异或后的数组.py
create_time: 2025/7/10 0:48
author: Ethan

Description: https://leetcode.cn/problems/decode-xored-array/description/
"""
from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        for i in encoded:
            first = i ^ first
            res.append(first)

        return res
