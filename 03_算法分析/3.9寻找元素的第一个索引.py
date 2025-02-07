"""
name: 3.9寻找元素的第一个索引
create_time: 2025/2/7 16:27
author: Ethan

Description: 
"""


def find(arr, target):
    """
    寻找元素的第一个索引, 时间复杂度为O(n)
    :param arr:
    :param target:
    :return:
    """
    n = len(arr)
    for i in range(n):
        if arr[i] == target:
            return i
    return -1