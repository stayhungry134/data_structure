"""
name: 09_回文数
create_time: 2023/7/9 21:27
author: Ethan

Description: 给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

例如，121 是回文，而 123 不是。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/palindrome-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def is_palindrome(x: int) -> bool:
    num_str = str(x)
    num_len = len(num_str)
    for i in range(num_len // 2):
        if num_str[i] != num_str[-i - 1]:
            return False
    return True


def is_palindrome1(x: int) -> bool:
    original_x = x
    reverse_x = 0
    while x > 0:
        reverse_x = reverse_x * 10 + x % 10
        x = x // 10
    return original_x == reverse_x


num = 121
print(is_palindrome1(num))
