"""
name: 4.12使用重复的平方计算幂函数
create_time: 2025/2/12 9:50
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
        partial = power(x, n // 2)
        result = partial * partial
        if n % 2 == 1:
            result *= x
        return result
