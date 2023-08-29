"""
name: 14_最长公共前缀
create_time: 2023/7/9 22:16
author: Ethan

Description: 编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""
"""

"""
心得: 
1. 首先考虑不到位的地方是一些边界条件，比如某个字符串为空或者只有一个元素，会出现索引超出的情况
2. 其次是有两层循环，可能会出现只有部分元素比较的情况
3. 最后是如何在所有元素都达成前面部分相等的情况下才去更新公共前缀
"""


def longest_common_prefix(strs: list[str]) -> str:
    strs_len = len(strs)
    str0_len = len(strs[0])
    result = ''
    # 如果只有一个字符串
    if strs_len == 1:
        return strs[0]
    for j in range(str0_len):
        for i in range(1, strs_len):
            l1 = strs[i][:j + 1]
            l2 = strs[0][:j + 1]
            if l1 != l2:
                return result
            else:
                if i == strs_len - 1:
                    result = strs[0][:j + 1]
    return result


# def longest_common_prefix(strs):
#     if not strs:
#         return ""
#
#     # 遍历第一个字符串的每个字符
#     for i in range(len(strs[0])):
#         char = strs[0][i]
#
#         # 在其他字符串的相同位置进行比较
#         for j in range(1, len(strs)):
#             # 如果其他字符串长度不足或者字符不相等，返回前缀
#             if i >= len(strs[j]) or strs[j][i] != char:
#                 return strs[0][:i]
#
#     # 如果遍历完第一个字符串的所有字符，说明第一个字符串是最长公共前缀
#     return strs[0]
#
# # 测试代码
# strs = ["flower", "flow", "flight"]
# result = longest_common_prefix(strs)
# print(result)

#
strs = ["a","b"]
print(longest_common_prefix(strs))

