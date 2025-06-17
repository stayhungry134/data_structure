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

    def differenceOfSums2(self, n: int, m: int) -> int:
        # 使用数学推导
        # num2 = m + m*2+ ... + m*k
        # num1 = 1 + 2 + ... + n - num2
        # res就等于 1加到n 减去两倍的 num2
        k = n // m
        return n * (n + 1) // 2 - k * (k + 1) * m