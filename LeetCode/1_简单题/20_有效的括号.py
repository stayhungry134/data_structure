"""
name: 20_有效的括号
create_time: 7/11/2023 2:37 PM
author: Ethan

Description: 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

1. 左括号必须用相同类型的右括号闭合。
2. 左括号必须以正确的顺序闭合。
3. 每个右括号都有一个对应的相同类型的左括号。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def is_valid(s: str) -> bool:
    dic = {
        ')': '(',
        ']': '[',
        '}': '{',
    }
    ls = []
    for item in s:
        # 如果是右括号
        if dic.get(item):
            try:
                stack_top = ls.pop()
                if stack_top == dic.get(item):
                    continue
                else:
                    return False
            except IndexError:
                return False
        # 如果是左括号
        else:
            ls.append(item)
    if len(ls) == 0:
        return True
    else:
        return False


s = "([)]{}"
print(is_valid(s))
