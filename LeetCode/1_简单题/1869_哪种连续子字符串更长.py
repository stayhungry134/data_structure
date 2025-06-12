"""
name: 1869_哪种连续子字符串更长.py
create_time: 2025/6/12 17:27
author: Ethan

Description: https://leetcode.cn/problems/longer-contiguous-segments-of-ones-than-zeros/description/
"""


class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        res_map = {
            0: 0,
            1: 0,
        }
        tem_map = {
            0: 0,
            1: 0,
        }
        for c in s:
            if c == '1':
                tem_map[1] += 1
                tem_map[0] = 0
                res_map[1] = max(tem_map[1], res_map[1])
            else:
                tem_map[0] += 1
                tem_map[1] = 0
                res_map[0] = max(tem_map[0], res_map[0])
        return res_map[1] > res_map[0]
