"""
name: 4.6测试元素唯一性
create_time: 2025/2/11 11:38
author: Ethan

Description: 
"""
def unique3(S, start, stop):
    """
    检查S[start:stop]中的元素是否唯一
    :param S:
    :param
    :param stop:
    :return:
    """
    if stop - start <= 1:
        return True
    elif not unique3(S, start, stop - 1):
        return False
    elif not unique3(S, start + 1, stop):
        return False
    else:
        return S[start] != S[stop - 1]
