"""
name: 2910_合法分组的最少组数.py
create_time: 2025/6/5 23:44
author: Ethan

Description: 
"""
from typing import List

class Solution:
    def minGroupsForValidAssignment(self, balls: List[int]) -> int:
        from collections import Counter
        import math
        res = 0
        # 对所有的balls进行统计
        ball_counter = Counter(balls)
        # 找到其中出现次数最少的那个
        values = ball_counter.values()
        min_count = min(values)
        for count in range(min_count, 0, -1):
            ans = 0
            for i in values:
                q, r = divmod(i, count)
                if q < r:
                    break
                ans += (count + i) // (count + 1)
            else:
                return ans
        return res




balls = [1,1,3,3,1,1,2,2,3,1,3,2]
# balls = [1,1,3,1,1,3]

print(Solution().minGroupsForValidAssignment(balls))
