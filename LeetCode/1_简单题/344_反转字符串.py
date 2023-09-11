"""
name: 344_反转字符串
create_time: 2023/9/5 16:22
author: Ethan

Description: 编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。

不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
"""


def reverse_string(s: list[str]) -> None:
    """
    也可以使用双指针法，一个指向 0，一个指向 s_len，两个相遇的时候终止，
    :param s:
    :return:
    """
    s_len = len(s)
    for i in range(s_len // 2):
        tem = s[i]
        # 如果是不支持 负数索引 的语言，则可以使用 len - i 来取到值
        s[i] = s[-i - 1]
        s[-i - 1] = tem