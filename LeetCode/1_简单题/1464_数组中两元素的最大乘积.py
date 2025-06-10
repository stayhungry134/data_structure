"""
name: 1464_数组中两元素的最大乘积.py
create_time: 2025/6/10 23:00
author: Ethan

Description: https://leetcode.cn/problems/maximum-product-of-two-elements-in-an-array/description/
"""
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums, reverse=True)
        return (sorted_nums[0] - 1) * (sorted_nums[1] - 1)


nums = [3,7]
print(Solution().maxProduct(nums))
