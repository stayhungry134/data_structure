"""
name: 
create_time: 2025/2/20 22:16
author: Ethan

Description: 使用递归，在不使用循环的情况下查找最大最小值
"""


def max_two(num1, num2):
    return num1 if num1 > num2 else num2


def min_two(num1, num2):
    return num1 if num1 < num2 else num2


def find_max(s):
    if len(s) == 1:
        return s[0]
    elif len(s) == 2:
        return max_two(s[0], s[2])
    else:
        return max_two(s[0], find_max(s[1:]))


def find_min(s):
    if len(s) == 1:
        return s[0]
    elif len(s) == 2:
        return min_two(s[0], s[2])
    else:
        return min_two(s[0], find_max(s[1:]))