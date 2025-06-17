"""
name: 2894_分类求和并作差.py
create_time: 2025/6/17 11:48
author: Ethan

Description: https://leetcode.cn/problems/divisible-and-non-divisible-sums-difference/description/
"""

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        ls1 = []
        ls2 = []
        for i in range(1, n+1):
            if i % m == 0:
                ls2.append(i)
            else:
                ls1.append(i)

        return sum(ls1) - sum(ls2)