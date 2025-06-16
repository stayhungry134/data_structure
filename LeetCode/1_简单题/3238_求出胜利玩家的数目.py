"""
name: 3238_求出胜利玩家的数目.py
create_time: 2025/6/16 16:26
author: Ethan

Description: https://leetcode.cn/problems/find-the-number-of-winning-players/description/
"""
from typing import List


class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        from collections import defaultdict
        tem_map = defaultdict(lambda: defaultdict(int))
        res = 0
        for x, y in pick:
            if not tem_map[x][y]:
                tem_map[x][y] = 0
            tem_map[x][y] += 1
        for user, dic in tem_map.items():
            yi = max(dic.values())
            if yi > user:
                res += 1
        return res

n = 4
pick = [[0,0],[1,0],[1,0],[2,1],[2,1],[2,0]]

print(Solution().winningPlayerCount(n, pick))