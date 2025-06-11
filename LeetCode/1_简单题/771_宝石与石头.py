"""
name: 771_宝石与石头.py
create_time: 2025/6/11 22:12
author: Ethan

Description: https://leetcode.cn/problems/jewels-and-stones/
"""

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        from collections import Counter
        stone_dic = Counter(stones)
        res = 0
        for jewel in jewels:
            res += stone_dic.get(jewel, 0)

        return res
