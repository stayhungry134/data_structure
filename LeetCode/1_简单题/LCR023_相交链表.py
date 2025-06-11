"""
name: LCR023_相交链表.py
create_time: 2025/6/11 22:16
author: Ethan

Description: 
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        map1 = {}
        point1 = headA
        point2 = headB
        while point1:
            map1[point1] = 1
            point1 = point1.next
        while point2:
            if map1.get(point2):
                return point2
            point2 = point2.next

        return None
