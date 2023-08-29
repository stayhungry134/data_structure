"""
name: 70_爬楼梯
create_time: 2023/8/3 17:38
author: Ethan

Description: 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
"""

dic = {}


def climb_stairs(n: int) -> int:
    if n == 1:
        dic[n] = 1
        return 1
    if n == 2:
        dic[n] = 2
        return 2
    if dic.get(n):
        return dic.get(n)
    if n > 2:
        result = climb_stairs(n - 1) + climb_stairs(n - 2)
        dic[n] = result
        return result


print(climb_stairs(99))