"""
name: 1927_求和游戏.py
create_time: 2025/7/8 21:56
author: Ethan

Description: https://leetcode.cn/problems/sum-game/description/
"""


class Solution:
    def sumGame(self, num: str) -> bool:
        len_n = len(num)
        left_sum = 0
        right_sum = 0
        left_q = 0
        right_q = 0
        half = len_n // 2
        for i, n in enumerate(num):
            if n.isdigit():
                if i < half:
                    left_sum += int(n)
                else:
                    right_sum += int(n)
            else:
                if i < half:
                    left_q += 1
                else:
                    right_q += 1

        diff = left_sum - right_sum

        return diff * 2 != (right_q - left_q) * 9

