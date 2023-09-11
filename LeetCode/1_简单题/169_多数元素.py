"""
name: 169_多数元素
create_time: 2023/9/6 14:17
author: Ethan

Description: 给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。
"""

def majority_element(nums: list[int]) -> int:
    dic = {}
    len_nums = len(nums)
    for num in nums:
        if dic.get(num):
            dic[num] += 1
        else:
            dic[num] = 1
    for key, val in dic.items():
        if val > len_nums / 2:
            return key

ls = [3,2,3]
print(majority_element(ls))
