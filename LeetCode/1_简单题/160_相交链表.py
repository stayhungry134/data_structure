"""
name: 160_相交链表
create_time: 2023/9/10 23:15
author: Ethan

Description: 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。
"""
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        dic = {}
        tem1 = headA
        while tem1:
            dic[tem1] = 1
            tem1 = tem1.next
        tem2 = headB
        while not dic.get(tem2):
            if tem2.next is None:
                return None
            tem2 = tem2.next
        return tem2
