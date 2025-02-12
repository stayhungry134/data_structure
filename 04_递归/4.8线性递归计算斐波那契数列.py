"""
name: 4.8线性递归计算斐波那契数列
create_time: 2025/2/11 11:43
author: Ethan

Description: 
"""
def good_fibonacci(n):
    """
    递归计算斐波那契数列
    :param n:
    :return:
    """
    if n <= 1:
        return n, 0
    else:
        (a, b) = good_fibonacci(n - 1)
        return a + b, a
