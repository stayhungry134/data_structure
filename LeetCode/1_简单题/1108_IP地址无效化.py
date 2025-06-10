"""
name: 1108_IP地址无效化.py
create_time: 2025/6/10 16:44
author: Ethan

Description: https://leetcode.cn/problems/defanging-an-ip-address/
"""
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')