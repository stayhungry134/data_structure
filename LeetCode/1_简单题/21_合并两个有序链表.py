"""
name: 21_合并两个有序列表
create_time: 7/11/2023 5:01 PM
author: Ethan

Description: 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1: list[int], list2: list[int]) -> list[int]:
    l1_len = len(list1)
    l2_len = len(list2)

    result = []
    i, j = 0, 0
    for k in range(l1_len + l2_len):
        print(i, j)
        # 如果第一个列表遍历完了
        if i >= l1_len:
            result += list2[j:]
            break
        # 如果第二个列表遍历完了
        if j >= l2_len:
            result += list1[i:]
            break
        if list1[i] >= list2[j]:
            result.append(list2[j])
            j += 1
        else:
            result.append(list1[i])
            i += 1
    return result


"""
使用递归来做
1. 考虑最小的情况，当其中一个链表为空时，可以直接返回另一个链表
2. 如果是其他情况，就使用递归，
如果是 list1 的值（可以理解为 list1 第一个元素的值，使用 list1.val取到） 大于 list2 的值时，就应该使用 list2 后面的值和 list1 的剩余值比较，所以就递归 list2.next
"""
def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if list1 is None:
        return list2
    elif list2 is None:
        return list1
    elif list1.val > list2.val:
        list2.next = mergeTwoLists(list1, list2.next)
        return list2
    else:
        list1.next = mergeTwoLists(list1.next, list2)
        return list1


l1 = [1, 2, 8, 8, 9, 10]
l2 = [1, 3, 9]
print(merge_two_lists(l1, l2))

