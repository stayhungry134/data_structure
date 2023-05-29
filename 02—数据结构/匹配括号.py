"""
File        : 匹配括号
IDE         ：PyCharm
Author      ：Ethan
Date        ：6/22/2022 7:10 PM
Description : 用来看括号是否匹配 ((()))()(()())
"""
from 栈Stack import Stack


def parChecker(symbolString):
    s = Stack()
    index = 0

    while index < len(symbolString):
        if symbolString[index] in '({[':
            s.push(symbolString[index])
        else:
            if s.isEmpty():
                return False
            else:
                s.pop()
        index += 1
    return s.isEmpty()


s1 = '((()))()(()({}))'
s2 = '((()))()(()({{}})))'
s3 = '(((()))()(()([][)))'

print(parChecker(s1))
print(parChecker(s2))
print(parChecker(s3))


