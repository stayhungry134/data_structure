"""
name: 58_最后一个单词的长度
create_time: 2023/7/27 11:59
author: Ethan

Description: 给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中 最后一个 单词的长度。

单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。
"""

def length_of_last_word(s: str) -> int:
    result = ''
    flag = False
    for letter in s:
        if letter == " ":
            flag = True
        else:
            if flag:
                result = letter
                flag = False
            else:
                result += letter

    return len(result)

def length_of_last_word1(s: str) -> int:
    result = 0
    flag = False
    for i in range(len(s)):
        if flag and s[-i - 1] == " ":
            return result
        elif s[-i - 1] != " ":
            flag = True
            result += 1
    return result


s = "a"
print(length_of_last_word(s))