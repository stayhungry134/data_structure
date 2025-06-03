"""
name: 1002_查找共用字符
create_time: 2025/6/3 23:31
author: Ethan

Description: https://leetcode.cn/problems/find-common-characters/
"""
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []

        res = []
        for c in words[0]:  # 遍历第一个单词的每个字符
            temp = True
            for j in range(1, len(words)):  # 从第2个单词开始
                if c in words[j]:
                    # 如果存在该字符，删除它的一次出现，防止重复匹配
                    words[j] = words[j].replace(c, '', 1)
                else:
                    # 如果某个单词中没有该字符，则标记为False
                    temp = False
                    break
            if temp:
                res.append(c)  # 所有单词都有这个字符，加到结果中

        return res


solution = Solution()

words = ["bella","label","roller"]

print(solution.commonChars(words))