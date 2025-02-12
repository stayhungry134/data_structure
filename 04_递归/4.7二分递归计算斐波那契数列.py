"""
name: 4.7二分递归计算斐波那契数列
create_time: 2025/2/11 11:41
author: Ethan

Description: 
"""


def bad_fibonacci(n):
    """
    递归计算斐波那契数列
    :param n:
    :return:
    """
    if n <= 1:
        return n
    else:
        return bad_fibonacci(n - 2) + bad_fibonacci(n - 1)
