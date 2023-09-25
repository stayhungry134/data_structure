"""
name: 705_设计哈希表集合
create_time: 2023/9/14 14:04
author: Ethan

Description: 不使用任何内建的哈希表库设计一个哈希集合（HashSet）。

实现 MyHashSet 类：

void add(key) 向哈希集合中插入值 key 。
bool contains(key) 返回哈希集合中是否存在这个值 key 。
void remove(key) 将给定值 key 从哈希集合中删除。如果哈希集合中没有这个值，什么也不做
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, head):
        self.head = head

    def find_node(self, target: int):
        tem_cell = self.head
        while tem_cell and tem_cell.val != target:
            tem_cell = tem_cell.next
        return tem_cell

    def find_pre_node(self, target: int):
        current = self.head
        while current and current.next:
            if current.next.val == target:
                return current
            current = current.next
        return None

    def del_node(self, target: int):
        if self.head is None:
            return

        if self.head.val == target:
            self.head = self.head.next
            return

        tem_cell = self.find_pre_node(target)
        if tem_cell is not None:
            tem_cell.next = tem_cell.next.next

    def add(self, target: int):
        node = Node(target)
        node.next = self.head
        self.head = node


class MyHashSet:

    def __init__(self):
        # 指定你一个 1000 大小的数组
        self.hash_data = [LinkedList(None) for _ in range(1000)]

    def add(self, key: int) -> None:
        # 如果已经有这个值，那么就不要添加
        if self.contains(key):
            return
        # 找到应该插入的位置，用要插入的数模1000，取到余数，然后余数就是它在数组的位置，如果在这个位置上已经有数据了，那么就用链表的形式
        locate: int = key % 1000
        if self.hash_data[locate] is None:
            self.hash_data[locate] = LinkedList(Node(key))
        else:
            self.hash_data[locate].add(key)

    def remove(self, key: int) -> None:
        locate: int = key % 1000
        self.hash_data[locate].del_node(key)

    def contains(self, key: int) -> bool:
        locate: int = key % 1000
        node = self.hash_data[locate].find_node(key)
        return bool(node)

