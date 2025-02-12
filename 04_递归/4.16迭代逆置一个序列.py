"""
name: 4.16迭代逆置一个序列
create_time: 2025/2/12 10:15
author: Ethan

Description: 
"""


def reverse_iterative(s):
    """
    reverse s里面的元素
    :param s:
    :return:
    """
    start, stop = 0, len(s)
    while start < stop - 1:
        s[start], s[stop] = s[stop - 1], s[start]
        start, stop = start + 1, stop - 1
