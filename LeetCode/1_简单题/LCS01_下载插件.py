"""
name: LCS01_下载插件.py
create_time: 2025/6/18 23:17
author: Ethan

Description: https://leetcode.cn/problems/Ju9Xwi/
"""

class Solution:
    def leastMinutes(self, n: int) -> int:
        width = 1
        res = 1
        while width < n:
            width *= 2
            res += 1
        return res

