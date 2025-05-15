"""
name: 2264_字符串中最大的3位相同数字
create_time: 2025/5/15 11:01
author: Ethan

Description: 
"""


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        low = 0
        quick = 1
        res_ls = []
        while quick < len(num):
            # 如果不是连续的
            if num[quick] != num[low]:
                low = quick
            # 如果连续3个一样
            if num[quick] == num[low] and quick - low == 2:
                res_ls.append(num[low]*3)
            quick += 1
        if not res_ls:
            return ''
        else:
            return max(res_ls)


solution = Solution()

num = "6777133339"

print(solution.largestGoodInteger(num))