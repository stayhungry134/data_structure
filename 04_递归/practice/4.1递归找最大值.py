"""
name: 
create_time: 2025/2/20 22:02
author: Ethan

Description: 含有 n 个元素的序列 S，递归算法找出最大值
"""


def find_max(s):
    if len(s) == 1:
        return s[0]
    elif len(s) == 2:
        if s[0] > s[1]:
            return s[0]
        else:
            return s[1]
    else:
        return max(s[0], find_max(s[1:]))
