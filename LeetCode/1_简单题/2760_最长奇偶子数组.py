"""
name: 2760_最长奇偶子数组
create_time: 2023/11/16 23:36
author: Ethan

Description: 给你一个下标从 0 开始的整数数组 nums 和一个整数 threshold 。

请你从 nums 的子数组中找出以下标 l 开头、下标 r 结尾 (0 <= l <= r < nums.length) 且满足以下条件的 最长子数组 ：

nums[l] % 2 == 0
对于范围 [l, r - 1] 内的所有下标 i ，nums[i] % 2 != nums[i + 1] % 2
对于范围 [l, r] 内的所有下标 i ，nums[i] <= threshold
以整数形式返回满足题目要求的最长子数组的长度。

注意：子数组 是数组中的一个连续非空元素序列。
"""


class Solution:
    def longestAlternatingSubarray(self, nums: list[int], threshold: int) -> int:
        result = 0
        nums_len = len(nums)
        cur = 0
        for i, num in enumerate(nums[cur:]):
            if num > threshold or num % 2 != 0:
                cur += 1
                continue
            j = i + 1
            while j < nums_len and nums[j] % 2 != nums[j-1] % 2 and nums[j] <= threshold:
                j += 1
            result = max(result, j - cur)
            cur += 1
        return result


nums = [1, 2]
threshold = 4

s = Solution()
print(s.longestAlternatingSubarray(nums, threshold))