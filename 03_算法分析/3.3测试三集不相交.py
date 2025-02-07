"""
name: 3.3测试三集不相交
create_time: 2025/2/7 15:59
author: Ethan

Description: 
"""


def disjoint1(A, B, C):
    """
    时间复杂度为O(n^3)的三集不相交
    :param A:
    :param B:
    :param C:
    :return:
    """
    for a in A:
        for b in B:
            for c in C:
                if a == b == c:
                    return False
    return True


def disjoint2(A, B, C):
    """
    时间复杂度为O(n^2)的三集不相交
    :param A:
    :param B:
    :param C:
    :return:
    """
    for a in A:
        for b in B:
            if a == b:
                for c in C:
                    if a == c:
                        return False
    return True


def disjoint3(A, B, C):
    """
    时间复杂度为O(n)的三集不相交
    :param A:
    :param B:
    :param C:
    :return:
    """
    for a in A:
        if a in B or a in C:
            return False
    for b in B:
        if b in C:
            return False
    return True
