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
        tem_grid = [num for row in grid for num in row]
        tem_k = k % len(tem_grid)
        pre = [num for num in tem_grid[-tem_k: ]]
        result_grid = tem_grid[-tem_k:] + tem_grid[:-tem_k]
        res = []
        for i in range(m):
            res.append(result_grid[i*n: (i+1)*n])
        return res[:m]


grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
k = 1

print(Solution().shiftGrid(grid, k))

