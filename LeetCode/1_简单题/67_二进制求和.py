"""
name: 67_二进制求和
create_time: 2023/7/31 10:23
author: Ethan

Description: 给你两个二进制字符串 a 和 b ，以二进制字符串的形式返回它们的和。
"""


def add_binary(a: str, b: str) -> str:
    result = []
    # 进位
    carry = 0
    a_len = len(a)
    b_len = len(b)
    max_len = max(a_len, b_len)
    for i in range(1, max_len + 1):
        a_num = int(a[-i]) if i <= a_len else 0
        b_num = int(b[-i]) if i <= b_len else 0
        num = a_num + b_num + carry
        if num > 1:
            result.append(str(num % 2))
            carry = num // 2
        else:
            result.append(str(num))
            carry = 0
    if carry == 1:
        result.append(str(carry))
    if carry == 2:
        result.extend(['1', '0'])
    result_str = ''.join(result[::-1])
    return result_str


a = "11"
b = "10"

print(add_binary(a, b))