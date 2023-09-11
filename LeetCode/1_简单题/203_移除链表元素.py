"""
name: 203_移除链表元素
create_time: 2023/9/11 21:51
author: Ethan

Description: 给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        def remove_next(node):
            if node.next:
                node.next = node.next.next
        while head and head.val == val:
            head = head.next
        tem = head
        while tem and tem.next is not None:
            if tem.next.val == val:
                remove_next(tem)
            else:
                tem = tem.next
        return head