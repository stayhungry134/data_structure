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


class MyHashSet:

    def __init__(self):
        pass

    def add(self, key: int) -> None:
        node = Node(key)
        node.next = self

    def remove(self, key: int) -> None:
        pass

    def contains(self, key: int) -> bool:
        pass



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
