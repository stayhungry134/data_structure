"""
name: 2656_K个元素的最大和
create_time: 2023/11/15 23:30
author: Ethan

Description: 给你一个下标从 0 开始的整数数组 nums 和一个整数 k 。你需要执行以下操作 恰好 k 次，最大化你的得分：

1. 从 nums 中选择一个元素 m 。
2. 将选中的元素 m 从数组中删除。
3. 将新元素 m + 1 添加到数组中。
4. 你的得分增加 m 。
请你返回执行以上操作恰好 k 次后的最大得分。
"""


class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        max_num = max(nums)
        return max_num * k + k * (k - 1) // 2