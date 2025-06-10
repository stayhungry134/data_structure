"""
name: 812_最大的三角形面积.py
create_time: 2025/6/10 17:11
author: Ethan

Description: https://leetcode.cn/problems/largest-triangle-area/
"""
from itertools import combinations
from typing import List

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def triangleArea(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int) -> float:

            # 这是三角形的一个面积公式
            # area = 0.5 * abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))
            return abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2
        # combinations 的作用就是从一个可迭代对象中选出指定数量的所有组合
        return max(triangleArea(x1, y1, x2, y2, x3, y3) for (x1, y1), (x2, y2), (x3, y3) in combinations(points, 3))

# 后面可以使用更高难度的凸包算法来计算
points = [[4,6],[6,5],[3,1]]
print(Solution().largestTriangleArea(points))