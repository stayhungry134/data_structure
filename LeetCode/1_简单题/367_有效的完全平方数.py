"""
name: 367_有效的完全平方数.py
create_time: 2025/6/10 16:47
author: Ethan

Description: https://leetcode.cn/problems/valid-perfect-square/
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num
        while left <= right:
            # 注意二分法这里mid的处理逻辑
            mid = left + (right - left) // 2
            tem_res = mid * mid
            # mid + 1 和 - 1 可以避免重复，同时推进left和right靠近，不至于陷入死循环
            if tem_res < num:
                left = mid + 1
            elif tem_res > num:
                right = mid - 1
            else:
                return True
        return False

num = 16
print(Solution().isPerfectSquare(num))
