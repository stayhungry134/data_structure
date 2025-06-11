"""
name: 2243_计算字符串的数字和.py
create_time: 2025/6/11 21:50
author: Ethan

Description: https://leetcode.cn/problems/calculate-digit-sum-of-a-string/
"""

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        if len(s) <= k:
            return s
        # 先分组
        nums = list(s)
        res_ls = []
        tem = []
        for i in range(len(nums)):
            tem.append(int(nums[i]))
            if (i + 1) % k == 0 or i == len(nums) - 1:
                res_ls.append(sum(tem))
                tem = []
        res = ''.join([str(i) for i in res_ls])
        if len(res) > k:
            return self.digitSum(res, k)
        else:
            return res


s = "233"
k = 3

print(Solution().digitSum(s, k))