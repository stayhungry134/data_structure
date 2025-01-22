"""
name: 2218_从栈中取出 K 个硬币的最大面值和
create_time: 2025/1/21 17:25
author: Ethan

Description: https://leetcode.cn/problems/maximum-value-of-k-coins-from-piles/description/
"""
from typing import List


class Solution:

    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        result = 0

        return result


if __name__ == '__main__':
    piles = [[37, 88], [51, 64, 65, 20, 95, 30, 26], [9, 62, 20], [44]]
    k = 9
    solution = Solution()
    answer = solution.maxValueOfCoins(piles, k)
    print(answer)
