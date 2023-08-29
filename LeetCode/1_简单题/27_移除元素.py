"""
name: 27_移除元素
create_time: 7/20/2023 4:12 PM
author: Ethan

Description: 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/remove-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
主要思路为双指针，
1. 遍历数组相当于指针每一次都向后移动一位
2. 而另一个指针在外面定义，只有当第一个指针遇到不和 val 相等的元素时，第二个指针才会向前。判断的依据就是 nums[一指针] !== nums[二指针]
"""
def remove_element(nums: list[int], val: int) -> int:
    len_nums = len(nums)
    k = 0
    for i in range(len_nums):
        if nums[i] == val:
            continue
        else:
            nums[k] = nums[i]
            k += 1
    nums[k:] = []
    return k


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2

print(remove_element(nums, val))
print(nums)
