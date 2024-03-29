"""
name: 3_无重复字符的最长子串
create_time: 2023/11/16 0:05
author: Ethan

Description: 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
"""





class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_dic = {}
        result = 0
        cur = 0
        tem_result = 0
        while cur < len(s):
            for letter in s[cur:]:
                tem_result += 1
                if s_dic.get(letter):
                    s_dic = {}  # 清空字典
                    tem_result = 0  # 重置临时结果
                    continue
                result = max(tem_result, result)
                s_dic[letter] = 1
                cur += 1
        return result


s = "jbpnbwwd"

solution = Solution()
print(solution.lengthOfLongestSubstring(s))