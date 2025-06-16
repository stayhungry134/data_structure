"""
name: 3238_求出胜利玩家的数目.py
create_time: 2025/6/16 16:26
author: Ethan

Description: https://leetcode.cn/problems/find-the-number-of-winning-players/description/
"""
from typing import List


class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        ls = [[0] * 11 for _ in range(n)]  # 因为题目中明确给了 y 是 0 到 10 之间
        res = set()
        # 可以使用二维数组来记录玩家的情况
        for x, y in pick:
            ls[x][y] += 1
            if ls[x][y] > x:
                res.add(x)
        return len(res)

n = 4
pick = [[0,0],[1,0],[1,0],[2,1],[2,1],[2,0]]

print(Solution().winningPlayerCount(n, pick))