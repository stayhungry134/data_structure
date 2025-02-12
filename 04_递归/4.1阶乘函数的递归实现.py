"""
name: 4.1阶乘函数的递归实现
create_time: 2025/2/11 10:32
author: Ethan

Description: 
"""


def factorial(n):
    """
    阶乘函数的递归实现
    :param n:
    :return:
    """
    if n == 0:
        return 1
    return n * factorial(n-1)