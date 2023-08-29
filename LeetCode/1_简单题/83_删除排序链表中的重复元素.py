"""
name: 83_删除排序链表中的重复元素
create_time: 2023/8/15 23:53
author: Ethan

Description: 
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_uplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    current = head
    if not head:
        return head
    while current.next:
        if not current.val ^ current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head


def list_to_link(ls):
    nodes = ListNode(ls[0])
    current = nodes
    for item in ls[1:]:
        tem_node = ListNode(item)
        current.next = tem_node
        current = current.next
    return nodes


head = [1, 1, 3, 4, 4, 5]

tem_head = list_to_link(head)

result = delete_uplicates(tem_head)

n = result
while n:
    print(n.val)
    n = n.next
