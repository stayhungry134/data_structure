"""
name: 3042_统计前后缀下标对I.py
create_time: 2025/6/16 17:20
author: Ethan

Description: https://leetcode.cn/problems/count-prefix-and-suffix-pairs-i/description/
"""
from typing import List

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res = 0
        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words[i+1:]):
                if word2.startswith(word1) and word2.endswith(word1):
                    res += 1
        return res


words = ["abab","ab"]

print(Solution().countPrefixSuffixPairs(words))
