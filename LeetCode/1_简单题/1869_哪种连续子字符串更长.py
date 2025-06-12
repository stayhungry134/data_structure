"""
name: 1869_哪种连续子字符串更长.py
create_time: 2025/6/12 17:27
author: Ethan

Description: https://leetcode.cn/problems/longer-contiguous-segments-of-ones-than-zeros/description/
"""


class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        n = len(s)
        len_0 = 1 if s[0] == '0' else 0
        len_1 = 1 if s[0] == '1' else 0
        tem_cnt = 0
        pre_c = ''
        for c in s:
            if c == pre_c:
                tem_cnt += 1
            else:
                if pre_c == '1':
                    len_1 = max(len_1, tem_cnt)
                else:
                    len_0 = max(len_0, tem_cnt)
                tem_cnt = 1
            pre_c = c
        if pre_c == '1':
            len_1 = max(tem_cnt, len_1)
        else:
            len_0 = max(tem_cnt, len_0)
        return len_1 > len_0


s = "0"

print(Solution().checkZeroOnes(s))
