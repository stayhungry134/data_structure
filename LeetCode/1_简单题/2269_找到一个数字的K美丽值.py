"""
name: 2269_找到一个数字的K美丽值.py
create_time: 2025/6/5 23:36
author: Ethan

Description: 
"""


class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_str = str(num)
        res = 0
        for i in range(len(num_str) - k + 1):
            # 切割字符串
            tem_str = num_str[i: i+k]
            tem_num = int(tem_str)
            # 计算时候能够被整除
            if tem_num != 0 and num % tem_num == 0:
                res += 1

        return res

print(Solution().divisorSubstrings(240, 2))
