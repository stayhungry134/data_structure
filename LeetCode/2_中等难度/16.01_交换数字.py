"""
name: 16.01_交换数字.py
create_time: 2025/7/4 23:46
author: Ethan

Description: https://leetcode.cn/problems/swap-numbers-lcci/
"""
from typing import List


class Solution:
    def swapNumbers(self, numbers: List[int]) -> List[int]:
        return numbers[::-1]

# 加减法 整数
def swap(numbers):
    numbers[0] = numbers[0] + numbers[1]
    numbers[1] = numbers[0] - numbers[1]
    numbers[0] = numbers[0] - numbers[1]
    return numbers


# 异或运算（仅适用于整数）
def swap(numbers):
    numbers[0] = numbers[0] ^ numbers[1]
    numbers[1] = numbers[0] ^ numbers[1]
    numbers[0] = numbers[0] ^ numbers[1]
    return numbers
