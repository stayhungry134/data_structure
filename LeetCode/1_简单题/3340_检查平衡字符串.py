"""
name: 3340_检查平衡字符串.py
create_time: 2025/7/8 21:50
author: Ethan

Description: https://leetcode.cn/problems/check-balanced-string/
"""


class Solution:
    def isBalanced(self, num: str) -> bool:
        sum1 = 0
        sum2 = 0
        for i in range(len(num)):
            if i % 2:
                sum1 += int(num[i])
            else:
                sum2 += int(num[i])

        return sum1 == sum2

