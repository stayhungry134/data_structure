"""
name: 119_杨辉三角2.py
create_time: 2025/6/17 11:33
author: Ethan

Description: https://leetcode.cn/problems/pascals-triangle-ii/
"""
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        pre_row = self.getRow(rowIndex-1)
        res_row = [1] * (rowIndex + 1)
        for i in range(len(pre_row) - 1):
            res_row[i+1] = pre_row[i] + pre_row[i+1]

        return res_row


