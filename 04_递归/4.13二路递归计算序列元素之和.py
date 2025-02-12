"""
name: 4.13二路递归计算序列元素之和
create_time: 2025/2/12 9:55
author: Ethan

Description: 
"""


def binary_sum(s, start, stop):
    """
    返回 s[start, stop] 的和
    :param s:
    :param start:
    :param stop:
    :return:
    """
    if start >= stop:
        return 0
    elif start == stop - 1:
        return s[start]
    else:
        mid = (start + stop) // 2
        return binary_sum(s, start, mid) + binary_sum(s. mid, stop)
