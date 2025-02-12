"""
name: 4.10线性递归逆置序列元素
create_time: 2025/2/11 11:57
author: Ethan

Description: 
"""


def reverse(S, start, stop):
    """
    递归逆置序列元素
    :param S:
    :param start:
    :param stop:
    :return:
    """
    if start < stop - 1:  # 如果序列中至少有两个元素
        S[start], S[stop - 1] = S[stop - 1], S[start]
        reverse(S, start + 1, stop - 1)
