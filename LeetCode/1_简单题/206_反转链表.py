"""
name: 206_反转链表
create_time: 2023/9/4 16:28
author: Ethan

Description: 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    pre = None
    cur = head
    while head is not None:
        tem = cur.next
        cur.next = pre
        pre = cur
        cur = tem
    return pre