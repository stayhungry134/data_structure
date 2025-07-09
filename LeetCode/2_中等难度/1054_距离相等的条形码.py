"""
name: 1054_距离相等的条形码.py
create_time: 2025/7/7 23:02
author: Ethan

Description: https://leetcode.cn/problems/distant-barcodes/description/
"""
from typing import List


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        from collections import Counter
        count = Counter(barcodes)
        sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=False)
        i = 0
        res = [0] * len(barcodes)
        while sorted_count:
            barcode, num = sorted_count.pop()
            # 先填充所有的偶数位置
            for _ in range(num):
                res[i] = barcode
                i += 2
                # 如果填充满了
                if i >= len(barcodes):
                    i = 1
        return res



barcodes = [1,1,1,1,2,2,3,3]
print(Solution().rearrangeBarcodes(barcodes))
