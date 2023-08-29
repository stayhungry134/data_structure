"""
name: 67_x的平方根
create_time: 2023/8/3 16:56
author: Ethan

Description: 给你一个非负整数 x ，计算并返回 x 的 算术平方根 。

由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。

注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。
"""


def my_sqrt(x: int) -> int:
    if x == 0 or x == 1:
        return x
    result = x / 2
    while result * result - 1 >= x:
        result = (result + x / result) / 2
    return int(result)

x = 8
print(my_sqrt(x))