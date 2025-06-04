"""
name: 1347_制造字母异位词的最小步骤数
create_time: 2025/6/4 23:20
author: Ethan

Description: 
"""


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        res = 0
        tem_map = {}
        for c in s:
            if not tem_map.get(c):
                tem_map[c] = 0
            tem_map[c] += 1
        for c in t:
            if tem_map.get(c):
                tem_map[c] -= 1
            else:
                res += 1

        return res
