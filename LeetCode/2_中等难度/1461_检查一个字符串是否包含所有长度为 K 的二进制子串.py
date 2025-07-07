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


class Solution2:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)

        # 情况一：长度不足k，肯定不可能包含任何k位子串
        if n < k:
            return False

        total = 1 << k  # 总共应该包含的不同子串数量：2^k

        # 情况二：窗口数量不足2^k个，不可能覆盖全部
        if n - k + 1 < total:
            return False

        mask = (1 << k) - 1  # 掩码，用来保留k位的低位部分。例如k=3时：mask = 0b111 = 7
        seen = [False] * total  # 创建布尔数组表示所有子串是否出现过，默认都是False
        num = 0  # 用于保存当前滑动窗口表示的整数值（滚动窗口二进制转十进制）

        # 第一步：初始化第一个窗口（前k位），构造num
        for i in range(k):
            num = (num << 1) | (1 if s[i] == '1' else 0)
            # 说明：每遇到一位就左移（相当于 *2），然后加上当前位（0或1）
            # 例如：s = "101", k = 3，构造过程：1 → 10 → 101，对应二进制值为 5

        seen[num] = True  # 标记第一个窗口对应的子串为已出现
        count = 1  # 当前已找到的不同子串数量

        # 如果一开始就命中了全部子串（通常不太可能），可以直接返回
        if count == total:
            return True

        # 第二步：滑动窗口开始移动，从第k位开始
        for i in range(k, n):
            # 滑动窗口：左移一位，并与掩码相与（保证只保留k位）
            num = (num << 1) & mask

            # 添加当前新位（s[i]），注意当前位为'1'时加1，否则加0
            if s[i] == '1':
                num |= 1

            # 如果当前新窗口的子串还没出现过，记录并更新计数
            if not seen[num]:
                seen[num] = True
                count += 1
                # 如果已找到全部2^k种子串，提前返回True
                if count == total:
                    return True

        # 如果遍历完整个字符串都没找到所有2^k个子串，返回False
        return False


s = "00110"
k = 2
print(Solution().hasAllCodes(s, k))
