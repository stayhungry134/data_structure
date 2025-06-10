"""
name: 1304_和为零的N各不同整数.py
create_time: 2025/6/10 17:42
author: Ethan

Description: https://leetcode.cn/problems/find-n-unique-integers-sum-up-to-zero/description/
"""
from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        # 如果n是1,直接返回
        if n == 1:
            return [0]
        for i in range(n // 2):
            res.append(-(i + 1))
            res.append(i + 1)
        # 如果n是奇数
        if n % 2 == 1:
            res.append(0)

        return res