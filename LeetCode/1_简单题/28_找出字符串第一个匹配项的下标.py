"""
name: 28_找出字符串第一个匹配项的下标
create_time: 2023/7/27 11:38
author: Ethan

Description: 给你两个字符串 haystack 和 needle ，
请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。
如果 needle 不是 haystack 的一部分，则返回  -1 。
"""


def str_str(haystack: str, needle: str) -> int:
    ha_len = len(haystack)
    ne_len = len(needle)
    if ne_len > ha_len:
        return -1
    def compare_needle(start):
        for i in range(ne_len):
            # if start + i >= ha_len:
            #     return False
            if needle[i] != haystack[start + i]:
                return False
        return True

    # for j in range(ha_len):
    for j in range(ha_len - ne_len + 1):
        # 如果第一个下标相同
        if haystack[j] == needle[0]:
            if haystack[j: j+ne_len] == needle:
                return j
            # if compare_needle(j):
            #     return j
    return -1

# TODO 进阶：KMP算法
haystack = "mississippi"
needle = "issippi"

print(str_str(haystack, needle))