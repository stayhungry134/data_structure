"""
name: 1748_唯一元素的和
create_time: 2025/6/4 23:46
author: Ethan

Description: 
"""
from typing import List

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        tem_map = {}
        for num in nums:
            if not tem_map.get(num):
                tem_map[num] = 0
            tem_map[num] += 1
        return sum([key for key, val in tem_map.items() if val == 1])