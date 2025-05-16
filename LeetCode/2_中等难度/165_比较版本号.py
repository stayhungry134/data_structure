"""
name: 165_比较版本号
create_time: 2025/5/16 11:42
author: Ethan

Description: 
"""


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1_ls = version1.split('.')
        version2_ls = version2.split('.')
        len1 = len(version1_ls)
        len2 = len(version2_ls)
        for i in range(min(len1, len2)):
            num1 = int(version1_ls[i])
            num2 = int(version2_ls[i])
            if num1 > num2:
                return 1
            if num1 < num2:
                return -1
        if len1 < len2:
            tem = [i for i in version2_ls[len1:] if int(i) != 0]
            if len(tem):
                return -1
        if len1 > len2:
            tem = [i for i in version1_ls[len2:] if int(i) != 0]
            if len(tem):
                return 1
        return 0


solution = Solution()
v1 = "1.0.1"
v2 = "1"

print(solution.compareVersion(v1, v2))