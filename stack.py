"""
name: stack
create_time: 2025/3/12 2025/3/12
author: Ethan

Description: 
"""

class Stack:
    def __init__(self):
        self._ls = []

    def push(self, ele):
        self._ls.append(ele)

    def pop(self):
        return self._ls.pop()

    def top(self):
        return self._ls[-1]

    def get_min(self):
        tem_min = self._ls[0]
        for i in self._ls[1:]:
            if i < tem_min:
                tem_min = i
        return tem_min


def binary_search(arr, target):
    # 假如是升序
    arr_len = len(arr)
    mid = arr_len // 2
    if arr[mid] > target:
        return binary_search(arr[:mid], target)
    elif arr[mid] < target:
        return binary_search(arr[mid + 1:], target)
    elif arr[mid] == target:
        return mid
    return -1