"""
name: 3330_找到初始输入字符串.py
create_time: 2025/6/18 23:39
author: Ethan

Description: https://leetcode.cn/problems/find-the-original-typed-string-i/description/
"""


class Solution:
    def possibleStringCount(self, word: str) -> int:
        res = 1
        for i in range(1, len(word)):
            if word[i] == word[i-1]:
                res += 1
        return res


word = "abbcccc"

print(Solution().possibleStringCount(word))