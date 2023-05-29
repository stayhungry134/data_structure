"""
File        : 栈Stack的实现
IDE         ：PyCharm 
Author      ：Ethan
Date        ：6/22/2022 2:16 PM 
Description : 使用 Python 列表实现一个栈，最先进去的，最后出来
"""


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

