"""
name: 58_最后一个单词的长度
create_time: 2023/7/27 11:59
author: Ethan

Description: 给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中 最后一个 单词的长度。

单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        flag = False
        for c in s[::-1]:
            if c != ' ':
                flag = True
                res += 1
            elif c == ' ' and flag == True:
                break
        return res

s = "   fly me   to   the moon  "
print(Solution().lengthOfLastWord(s))