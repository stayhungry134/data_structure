"""
File        : 队列
IDE         ：PyCharm 
Author      ：Ethan
Date        ：6/22/2022 8:53 PM 
Description : Python 使用列表来实现队列并不好，因为在列表头部插入和移除元素很慢，可以用双端队列
"""

from collections import deque

queue = deque('earth')

queue.append('es')
queue.appendleft('s')
queue.pop()
queue.popleft()
queue.remove('r')

