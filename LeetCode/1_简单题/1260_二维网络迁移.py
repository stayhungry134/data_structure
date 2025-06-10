"""
name: 1260_二维网络迁移.py
create_time: 2025/6/10 21:22
author: Ethan

Description: https://leetcode.cn/problems/shift-2d-grid/
"""
from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        tem = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                num = grid[i][j]
                add_i, add_j = divmod(k, n)
                # 防止超出行范围
                add_i1, result_j = divmod((j + add_j), n)
                result_i = (i + add_i + add_i1) % m
                tem[result_i][result_j] = num
        return tem


grid = [[1,2,3],[4,5,6],[7,8,9]]
k = 1

print(Solution().shiftGrid(grid, k))

