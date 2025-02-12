"""
name: 4.9线性递归计算序列元素的和
create_time: 2025/2/11 11:48
author: Ethan

Description: 
"""


def linear_sum(S, n):
    """
    递归计算序列元素的和
    :param S:
    :param n:
    :return:
    """
    if n == 0:
        return 0
    return linear_sum(S, n - 1) + S[n - 1]
