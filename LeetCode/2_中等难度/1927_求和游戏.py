"""
name: 1927_求和游戏.py
create_time: 2025/7/8 21:56
author: Ethan

Description: https://leetcode.cn/problems/sum-game/description/
"""


class Solution:
    def sumGame(self, num: str) -> bool:
        all_q = num.count('?')
        if all_q % 2 == 1:
            return True
        half = len(num) // 2
        left_sum = right_sum = 0
        left_q = right_q = 0
        for n in num[:half]:
            if n != '?':
                left_sum += int(n)
            else:
                left_q += 1
        for n in num[half:]:
            if n != '?':
                right_sum += int(n)
            else:
                right_q += 1

        return (left_sum - right_sum) * 2 != (right_q - left_q) * 9
