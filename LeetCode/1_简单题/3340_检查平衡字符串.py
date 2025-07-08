"""
name: 3340_检查平衡字符串.py
create_time: 2025/7/8 21:50
author: Ethan

Description: https://leetcode.cn/problems/check-balanced-string/
"""


class Solution:
    def isBalanced(self, num: str) -> bool:
        ls1 = []
        ls2 = []
        for i in range(len(num)):
            if i % 2 == 0:
                ls1.append(int(num[i]))
            else:
                ls2.append(int(num[i]))

        return sum(ls1) == sum(ls2)

