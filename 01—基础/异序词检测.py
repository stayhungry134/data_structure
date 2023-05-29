"""
File        : 异序词检测
IDE         ：PyCharm 
Author      ：Ethan
Date        ：6/21/2022 10:54 PM 
Description : 用来判断两个英文单词是否由相同的字母组成，且每个字母的个数相同
              比如 earth 和 heart
"""


# 清点法，O(n²)
def anagramSolution1(s1, s2):
    alist = list(s2)  # 转换为列表

    pos1 = 0  # 列表 1 的指针
    stillOK = True  # 判断是否一样的标志

    while pos1 < len(s1) and stillOK:  # 如果列表 1 指针还没有到达最后且没有出现找不到的字母
        pos2 = 0  # 列表 2 的指针
        found = False  # 定义一个变量来标识列表 1 的字母是否在列表 2 中存在
        while pos2 < len(alist) and not found:  # 如果指针还没有到达最后且 not found
            if s1[pos1] == alist[pos2]:  # 如果发现列表 1 中指针指向的数字在列表 2 中存在
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False
        pos1 = pos1 + 1
    return stillOK


# 排序法, O(n²)，排序占时间
def anagramSolution2(s1, s2):
    list1 = list(s1)
    list2 = list(s2)

    list1.sort()
    list2.sort()

    pos = 0
    stillOk = True
    while pos < len(s1) and stillOk:
        if list1[pos] == list2[pos]:
            pos += 1
        else:
            stillOk = False

    return stillOk


# 计数法，O(n²)
def anagramSolution3(s1, s2):
    list1 = [0] * 26
    list2 = [0] * 26

    stillOK = True
    pos = 0

    for i in s1:
        list1[ord(i) - ord('a')] += 1
    for i in s2:
        list2[ord(i) - ord('a')] += 1
    while pos < 26 and stillOK:
        if list1[pos] == list2[pos]:
            pos += 1
        else:
            stillOK = False

    return stillOK


str1 = 'heart'
str2 = 'earth'
str3 = 'marks'

print(anagramSolution1(str1, str2))
print(anagramSolution1(str1, str3))
print(anagramSolution2(str1, str2))
print(anagramSolution2(str1, str3))
print(anagramSolution3(str1, str2))
print(anagramSolution3(str1, str3))