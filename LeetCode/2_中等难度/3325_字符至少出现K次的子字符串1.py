"""
name: 3325_字符至少出现K次的子字符串1
create_time: 2025/5/15 11:22
author: Ethan

Description: 
"""


class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        res = 0
        n = len(s)
        if k == 1:
            res = n * ( n + 1) // 2
        else:
            low = 0
            quick = 2
            while low <= n:
                tem_dic = {}
                tem = s[low: quick]
                for c in s[low: quick]:
                    if tem_dic.get(c):
                        tem_dic[c] += 1
                    else:
                        tem_dic[c] = 1
                if tem_dic != {} and max(tem_dic.values()) >= k:
                    res += 1
                # 如果 quick 到头了
                if quick >= n:
                    low += 1
                    quick = low + 2
                else:
                    quick += 1
        return res


solution = Solution()

s = "qkfiuuhd"
k = 2

print(solution.numberOfSubstrings(s, k))