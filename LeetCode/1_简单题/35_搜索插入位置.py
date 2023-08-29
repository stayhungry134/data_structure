"""
name: 28_搜索插入位置
create_time: 7/20/2023 4:27 PM
author: Ethan

Description: 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/search-insert-position
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


"""
这里不必被二分法的一些递归解法拘束，需要注意的是，在后面逐渐二分的时候，应该基础之前mid的位置，然后再进行后续操作
"""
def search_insert(nums: list[int], target: int) -> int:
    len_nums = len(nums)
    # 需要记录左边，右边，和中间，开局假设目标索引在最末尾
    left = 0
    right = len_nums - 1
    ans = len_nums
    # 当左右节点相遇的时候，表明找到了目标
    while left <= right:
        # 这里注意要加上 left，这样才能算出其在整个列表中的索引
        mid = (right - left) // 2 + left
        if target <= nums[mid]:
            # 这里将 mid 赋值给目标索引，当左右节点相遇的时候，就可以直接返回目标索引
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans


nums = [1, 3, 5, 6, 9, 12]
target = 13
print(search_insert(nums, target))