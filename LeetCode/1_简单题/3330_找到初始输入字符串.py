"""
name: 3330_找到初始输入字符串.py
create_time: 2025/6/18 23:39
author: Ethan

Description: https://leetcode.cn/problems/find-the-original-typed-string-i/description/
"""


class Solution:
    def possibleStringCount(self, word: str) -> int:
        pre_c = word[0]
        res_ls = []
        tem_cnt = 0
        for c in word[1:]:
            # 如果当前单词与它前一个单词相同
            if c == pre_c:
                tem_cnt += 1
            else:
                if tem_cnt > 0:
                    res_ls.append(tem_cnt)
                    tem_cnt = 0
            pre_c = c
        res_ls.append(tem_cnt)
        return sum(res_ls) + 1


word = "abbcccc"

print(Solution().possibleStringCount(word))