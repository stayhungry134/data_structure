"""
name: 1365_有多少小于当前数字的数字.py
create_time: 2025/6/13 23:42
author: Ethan

Description: https://leetcode.cn/problems/how-many-numbers-are-smaller-than-the-current-number/
"""
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        tem_dic = {}
        res = []
        # 这里循环之后(从小到大)，就可以得到每一个数字之前有几个比它小的
        for i, num in enumerate(sorted_nums):
            if num not in tem_dic: # 对于那些相同的数，因为之前已经存了，所以不会多次存
                tem_dic[num] = i
        for i, num in enumerate(nums):
            res.append(tem_dic.get(num, 0))

        return res


nums = [8,1,2,2,3]

print(Solution().smallerNumbersThanCurrent(nums))