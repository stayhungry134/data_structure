"""
File        : 括号校验
IDE         ：PyCharm 
Author      ：Ethan
Date        ：6/22/2022 9:11 PM 
Description : 
"""


def isValid(s):
    ls = []
    index = 0

    while index < len(s):
        # 实现一个栈，如果是 ([{，将其加入到列表中
        if s[index] in '({[':
            ls.append(s[index])
        else:
            # 如果不是 ([{，且列表为空，不匹配
            if ls == []:
                return False
            # 列表不为空，取出来
            else:
                top = ls.pop()
                if not matches(top, s[index]):
                    return False
        index += 1
    return ls ==[]


# 可能出现 [} 的情况
def matches(open, close):
    opens = "([{"
    closes = ")]}"

    return opens.index(open) == closes.index(close)