"""
name: 3.1find_max
create_time: 2025/2/7 15:53
author: Ethan

Description: 返回最大值的函数
"""


def find_max(nums):
    """
    返回最大值的函数
    :param nums:
    :return:
    """
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num
