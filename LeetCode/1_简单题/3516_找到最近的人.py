"""
name: 3516_找到最近的人.py
create_time: 2025/6/10 0:09
author: Ethan

Description: https://leetcode.cn/problems/find-closest-person/
"""


class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        diff1 = abs(x - z)
        diff2 = abs(y - z)
        if diff1 < diff2:
            return 1
        elif diff1 > diff2:
            return 2
        else:
            return 0

