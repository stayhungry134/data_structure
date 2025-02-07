"""
name: 3.4测试元素唯一性
create_time: 2025/2/7 16:12
author: Ethan

Description: 
"""


def unique1(nums):
    """
    时间复杂度为O(n^2)的测试元素唯一性
    :param nums:
    :return:
    """
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] == nums[j]:
                return False
    return True


def unique2(nums):
    """
    时间复杂度为O(nlogn)的测试元素唯一性
    :param nums:
    :return:
    """
    temp = sorted(nums)
    n = len(temp)
    for i in range(n-1):
        if temp[i] == temp[i+1]:
            return False
    return True
