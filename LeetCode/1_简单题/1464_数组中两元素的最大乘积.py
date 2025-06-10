"""
name: 1464_数组中两元素的最大乘积.py
create_time: 2025/6/10 23:00
author: Ethan

Description: https://leetcode.cn/problems/maximum-product-of-two-elements-in-an-array/description/
"""
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        two_num = nums[:2]
        for num in nums[2: ]:
            if num > min(two_num):
                two_num = [num, max(two_num)]
        return (two_num[0] - 1) * (two_num[1] - 1)


nums = [3,7]