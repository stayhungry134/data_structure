"""
name: 4.11递归计算幂函数
create_time: 2025/2/12 9:48
author: Ethan

Description: 
"""


def power(x, n):
    """
    计算 x**n
    :param x:
    :param n:
    :return:
    """
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)
