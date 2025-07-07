"""
name: 1461_检查一个字符串是否包含所有长度为 K 的二进制子串.py
create_time: 2025/7/7 22:25
author: Ethan

Description: https://leetcode.cn/problems/check-if-a-string-contains-all-binary-codes-of-size-k/description/
"""


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        tem_set = set()
        for i in range(len(s) - k + 1):
            tem_s = s[i: i+k]
            tem_set.add(tem_s)
        print(tem_set)
        return len(tem_set) >= 1 << k

class Solution1:
    def hasAllCodes(self, s: str, k: int) -> bool:
        need = 1 << k  # 2^k
        seen = set()
        cur = 0
        for i in range(len(s)):
            cur = ((cur << 1) & ((1 << k) - 1)) | int(s[i])
            if i >= k - 1:
                seen.add(cur)
                if len(seen) == need:
                    return True
        return False


s = "00110"
k = 2
print(Solution().hasAllCodes(s, k))
