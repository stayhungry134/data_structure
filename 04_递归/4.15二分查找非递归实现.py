"""
name: 4.15二分查找非递归实现
create_time: 2025/2/12 10:09
author: Ethan

Description: 
"""


def binary_search_iterative(data, target):
    """
    如果target在data中，返回True
    :param data:
    :param target:
    :return:
    """
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return False
