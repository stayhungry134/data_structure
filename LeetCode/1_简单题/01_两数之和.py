"""
name: 01_两数之和
create_time: 2023/5/29 17:32
author: Ethan

Description: LeetCode 上面的题目，两数之和
"""
from typing import List


def two_sum(nums, target):
    diff_dic = {}
    for i, num in enumerate(nums):
        if diff_dic.get(num) != None and diff_dic.get(num) == num:
            return [nums.index(num), i]
        diff_dic[num] = target - num
    for num in nums:
        if diff_dic.get(diff_dic.get(num)) and nums.index(num) != nums.index(diff_dic[num]):
            return [nums.index(num), nums.index(diff_dic[num])]
    return None


def two_sum1(nums: list[int], target: int) -> list[int]:
    n = len(nums)
    harsh_table = dict()
    for i in range(n):
        if target - nums[i] in harsh_table:
            return [harsh_table[target - nums[i]], i]
        else:
            harsh_table[nums[i]] = i
    return []


nums = [1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 7, 1, 1, 1, 1, 1]
target = 11

# print(two_sum1(nums, target))


# 2023 年 7 月 2 日
def two_sum2(nums: list, target: int) -> list:
    hash_dic = dict()
    for index, num in enumerate(nums):
        diff_num = target - num
        if hash_dic.get(diff_num) is not None:
            return [hash_dic.get(diff_num), index]
        hash_dic[num] = index
    return []


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tem_dic = {}
        for i, num in enumerate(nums):
            diff_num = target - num
            if tem_dic.get(diff_num) is not None:
                return [tem_dic.get(diff_num), i]
            tem_dic[num] = i
        return []


nums = [2, 7, 11, 15]
target = 9
s = Solution()
print(s.twoSum(nums, target))


