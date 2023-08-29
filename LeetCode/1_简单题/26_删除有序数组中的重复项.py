"""
name: 26_删除有序数组中的重复项
create_time: 7/20/2023 3:56 PM
author: Ethan

Description: 给你一个 升序排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。

考虑 nums 的唯一元素的数量为 k ，你需要做以下事情确保你的题解可以被通过：

更改数组 nums ，使 nums 的前 k 个元素包含唯一元素，并按照它们最初在 nums 中出现的顺序排列。nums 的其余元素与 nums 的大小不重要。
返回 k 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/remove-duplicates-from-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def remove_duplicates(nums: list[int]) -> int:
    """
    需要改变原数组 nums，同时需要返回最后的长度
    """
    k = 0
    for num in nums:
        if num == nums[k]:
            continue
        else:
            k += 1
            nums[k] = num
    # print(nums[k + 1:])
    nums[k + 1:] = []
    return k + 1


nums = [1, 1, 2]
print(remove_duplicates(nums))
print(nums)