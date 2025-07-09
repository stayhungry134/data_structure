"""
name: 1961_检查字符串是否为数组前缀.py
create_time: 2025/7/10 0:56
author: Ethan

Description: https://leetcode.cn/problems/check-if-string-is-a-prefix-of-array/description/
"""
from typing import List


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        tem_str = s
        for word in words:
            if tem_str.startswith(word):
                tem_str = tem_str[len(word):]
            elif tem_str == '':
                return True
            else:
                return False
        if tem_str == '':
            return True
        return False
