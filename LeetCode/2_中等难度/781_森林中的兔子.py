"""
name: 781_森林中的兔子
create_time: 2025/4/20 22:25
author: Ethan

Description: 森林中有未知数量的兔子。提问其中若干只兔子 "还有多少只兔子与你（指被提问的兔子）颜色相同?" ，将答案收集到一个整数数组 answers 中，其中 answers[i] 是第 i 只兔子的回答。

给你数组 answers ，返回森林中兔子的最少数量。
"""
from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        from collections import Counter
        count = Counter(answers)
        res = 0
        for x, cnt in count.items():
            res += ((cnt + x) // (x + 1)) * (x + 1)
        return res


solution = Solution()
print(solution.numRabbits([0,0,1,1,1]))