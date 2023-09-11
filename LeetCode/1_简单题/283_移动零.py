"""
name: 283_移动零
create_time: 2023/9/5 16:34
author: Ethan

Description: 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。
"""


def move_zeroes(nums: list[int]) -> None:
    """
    使用双指针的方法实现
    """
    cur = 0
    tem = 0

    def swap(ls, i, j):
        tem = ls[i]
        ls[i] = ls[j]
        ls[j] = tem

    len_nums = len(nums)
    for i in range(len_nums):
        if nums[i] != 0:
            if tem != cur:
                swap(nums, cur, tem)
            cur += 1
            tem += 1
            continue
        else:
            cur += 1
    nums[tem: cur] = [0] * (cur - tem)


def move_zeroes1(nums: list[int]) -> None:
    """
    使用双指针的方法实现
    """
    tem = cur = 0
    while cur < len(nums):
        if nums[cur] != 0:
            nums[tem], nums[cur] = nums[cur], nums[tem]
            tem += 1
        cur += 1