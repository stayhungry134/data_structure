"""
name: 4.3二分查找
create_time: 2025/2/11 10:40
author: Ethan

Description: 
"""
def binary_search(data, target, low, high):
    """
    二分查找
    :param data:
    :param low:
    :param high:
    :return:
    """
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data. target, mid + 1, high)