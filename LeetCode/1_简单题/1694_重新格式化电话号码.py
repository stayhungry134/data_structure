"""
name: 1694_重新格式化电话号码
create_time: 2025/5/16 13:44
author: Ethan

Description: 
"""


class Solution:
    def reformatNumber(self, number: str) -> str:
        nums = [n for n in number if n.isdigit()]
        res_ls = []
        for i, n in enumerate(nums):
            res_ls.append(n)
            if i % 3 == 2:
                res_ls.append('-')
        if res_ls[-1] == '-':
            res_ls.pop()
        if res_ls[-2] == '-':
            res_ls.pop(-2)
            res_ls.insert(-2, '-')
        return ''.join(res_ls)

solution = Solution()
number = "1-23-45 6"
print(solution.reformatNumber(number))