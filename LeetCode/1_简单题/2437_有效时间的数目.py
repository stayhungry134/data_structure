"""
name: 2437_有效时间的数目.py
create_time: 2025/7/10 0:28
author: Ethan

Description: https://leetcode.cn/problems/number-of-valid-clock-times/description/
"""

class Solution:
    def countTime(self, time: str) -> int:
        tem_ls = [1] * 4
        for i, t in enumerate(time):
            if t == '?':
                if i == 0:
                    if time[1] == '?' or int(time[1]) < 4:
                        tem_ls[0] = 3
                    else:
                        tem_ls[0] = 2
                elif i == 1:
                    if time[0] == '?':
                        tem_ls[0] = 2
                        tem_ls[1] = 12
                    elif int(time[0]) < 2:
                        tem_ls[1] = 10
                    else:
                        tem_ls[1] = 4
                elif i == 3:
                    tem_ls[2] = 6
                elif i == 4:
                    tem_ls[3] = 10
        res = tem_ls[0]
        print(tem_ls)
        for i in tem_ls[1: ]:
            res *= i
        return res

time = '??:??'

print(Solution().countTime(time))