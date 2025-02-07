"""
name: 3.2前缀平均数
create_time: 2025/2/7 15:54
author: Ethan

Description: 前缀平均值（Prefix Average） 是指一个序列中每个元素的平均值，前缀平均值是在给定序列的前 𝑘k 个元素的平均值.
简单来说，前缀平均值是在序列的前 k 项数据上计算的平均值。比如[1, 2, 3, 4, 5]的前缀平均值为[1, 1.5, 2, 2.5, 3]。
"""


def prefix_average1(nums):
    """
    时间复杂度为O(n^2)的前缀平均值
    :param nums:
    :return:
    """
    n = len(nums)
    result = [0] * n
    for i in range(n):
        total = 0
        for j in range(i + 1):
            total += nums[j]
    return result


def prefix_average2(nums):
    """
    时间复杂度为O(n^2)的前缀平均值
    :param nums:
    :return:
    """
    n = len(nums)
    result = [0] * n
    for i in range(n):
        result[i] = sum(nums[0:i+1])/(i+1)
    return result


def prefix_average3(nums):
    """
    时间复杂度为O(n)的前缀平均值
    :param nums:
    :return:
    """
    n = len(nums)
    result = [0] * n
    total = 0
    for i in range(n):
        total += nums[i]
        result[i] = total/(i+1)
    return result