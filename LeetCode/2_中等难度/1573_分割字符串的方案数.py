"""
name: 1573_分割字符串的方案数.py
create_time: 2025/7/4 17:08
author: Ethan

Description: https://leetcode.cn/problems/number-of-ways-to-split-a-string/
"""
class Solution:
    def numWays(self, s: str) -> int:
        # 计算1的个数
        count = s.count('1')
        MOD = 10 ** 9 + 7
        # 如果全是0
        if count == 0:
            return (len(s) - 1) * (len(s) - 2) // 2 % MOD
        # 如果都不能等分为3部分，直接为0
        avg_1, n = divmod(count, 3)
        if n != 0:
            return 0
        tem_ls = [0, 0, 0]  # 记录三等分的1的个数
        num1, num2 = 0, 0
        flag = 0  #
        for c in s:
            if c == '1':
                if tem_ls[flag] == avg_1:
                    if flag == 2:
                        break
                    flag += 1
                tem_ls[flag] += 1
            if c == '0' and tem_ls[flag] == avg_1:
                if flag == 0:
                    num1 += 1
                elif flag == 1:
                    num2 += 1
        res = (num1 + 1) * (num2 + 1) % MOD
        return res
