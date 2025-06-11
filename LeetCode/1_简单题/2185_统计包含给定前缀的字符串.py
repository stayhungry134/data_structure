"""
name: 2185_统计包含给定前缀的字符串.py
create_time: 2025/6/11 21:47
author: Ethan

Description: https://leetcode.cn/problems/counting-words-with-a-given-prefix/
"""
from typing import List

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0
        for word in words:
            if word.startswith(pref):
                res += 1

        return res
