"""
File        : 两数之和
IDE         ：PyCharm 
Author      ：Ethan
Date        ：6/22/2022 9:20 PM 
Description : 
"""


def twoSum(nums, target):
    num_map = {}

    # 建立一个字典存储 target 与元素的差
    for i in nums:
        num_map[i] = target - i

    for key in num_map:
        try:
            num_map.get(num_map[key])
            # 如果两个数相等，比如[3, 3]
            # if nums.index(key) != nums.index(num_map[key]):
            #     return nums.index(key), nums.index(num_map[key])
        #     else:
        #         index1 = nums.index(key)
        #         nums.remove(key)
        #         return index1, nums.index(num_map[key]) + 1
        # except:
        #     continue


def twoSum1(nums, target):
    num_map = {}

    # 建立一个字典存储 target 与元素的差
    for i in nums:
        num_map[i] = target - i

    for key in num_map:
        if num_map[key] in num_map:
            if nums.index(key) != nums.index(num_map[key]):
                return nums.index(key), nums.index(num_map[key])
            else:
                index1 = nums.index(key)
                nums.remove(key)
                return index1, nums.index(num_map[key]) + 1
        else:
            continue


l = [4, 3, 3, 5]
ll = twoSum(l, 6)
# print(l.index(ll[0]), l.index(ll[1]))
print(ll)