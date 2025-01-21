"""
name: 3_无重复字符的最长子串
create_time: 2023/11/16 0:05
author: Ethan

Description: 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 哈希集合用于存储当前窗口的字符
        seen = set()
        left = 0  # 滑动窗口左边界
        max_length = 0  # 记录最长子串的长度

        for right in range(len(s)):
            # 如果字符重复，则移动左边界直到不重复
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            # 将当前字符加入集合
            seen.add(s[right])
            # 更新最大长度
            max_length = max(max_length, right - left + 1)

        return max_length


s = "abba"

solution = Solution()
print(solution.lengthOfLongestSubstring(s))