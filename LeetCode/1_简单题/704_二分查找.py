"""
name: 704_二分查找
create_time: 2023/9/5 17:03
author: Ethan

Description: 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，
写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
"""
from re import search
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right = len(nums) - 1
        left = 0
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                right = mid - 1
            if target > nums[mid]:
                left = mid + 1
        return -1

solution = Solution()
nums = [-1,0,3,5,9,12]
target = 9

print(solution.search(nums, target))