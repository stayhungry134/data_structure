"""
name: 88_合并两个有序数组
create_time: 2023/8/30 0:11
author: Ethan

Description: 给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。

请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。

注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n
"""


def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    while n > 0:
        # 如果 nums1 当中已经比较完了
        if m == 0:
            nums1[: n] = nums2[: n]
            break
        # 如果nums1指针大，nums1指针移动到最后, nums1指针往前移动
        if nums1[m - 1] > nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
        # 如果nums2指针大，nums2指针移动到最后, nums2指针往前移动
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
    print(nums1)


nums1 = [2, 0]
m = 1
nums2 = [1]
n = 1

merge(nums1, m, nums2, n)
