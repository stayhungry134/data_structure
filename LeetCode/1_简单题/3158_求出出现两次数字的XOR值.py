"""
name: 3158_求出出现两次数字的XOR值.py
create_time: 2025/6/25 0:06
author: Ethan

Description: https://leetcode.cn/problems/find-the-xor-of-numbers-which-appear-twice/description/
"""
from typing import List


class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        tem_map = {}
        for num in nums:
            if num not in tem_map:
                tem_map[num] = 1
            else:
                tem_map[num] += 1
        res = 0
        for i in [k for k, v in tem_map.items() if v == 2]:
            res = res ^ i

        return res


nums = [1, 2, 1, 3]

print(Solution().duplicateNumbersXOR(nums))