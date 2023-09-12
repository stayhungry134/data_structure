"""
name: 234_回文链表
create_time: 2023/9/12 22:22
author: Ethan

Description: 给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 快慢指针，找到中点，然后反转后半部分
        half_node = self.find_half(head)
        first_start = head
        second_start = self.reverse_list(half_node)
        result = True

        while result and second_start != None:
            if first_start.val != second_start.val:
                return False
            first_start = first_start.next
            second_start = second_start.next
        return result

    def find_half(self, head):
        slow = head
        quick = head
        while quick and quick.next is not None:
            slow = slow.next
            quick = quick.next.next
        return slow


    def reverse_list(self, head):
        pre = None
        cur = head
        while cur is not None:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        return pre
