"""
name: 61_加一
create_time: 2023/7/28 15:58
author: Ethan

Description: 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。
"""


def plus_one(digits: list[int]) -> list[int]:
    digits[-1] += 1
    if digits == [10]:
        return [1, 0]
    len_d = len(digits)
    flag = False
    for i in range(len_d):
        if digits[-i] == 10:
            digits[-i] = 0
            digits[-i-1] += 1
            flag = False
        else:
            if flag:
                break
            else:
                flag = True
                continue
    if digits[0] == 10:
        digits[0] = 0
        digits.insert(0, 1)
    return digits


digits = [9]
print(plus_one(digits))