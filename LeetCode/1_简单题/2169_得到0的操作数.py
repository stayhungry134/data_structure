"""
name: 2169_得到0的操作数
create_time: 2025/6/2 23:08
author: Ethan

Description: 
"""


class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        res_count = 0
        while num1 != 0 and num2 != 0:
            if num1 >= num2:
                num1 = num1 - num2
            else:
                num2 = num2 - num1
            res_count += 1
        return res_count

    def countOperations1(self, num1: int, num2: int) -> int:
        res_count = 0
        while num1 and num2:
            res_count += num1 // num2
            num1 %= num2
            num1, num2 = num2, num1

        return res_count


solution = Solution()

num1 = 10
num2 = 10

print(solution.countOperations(num1, num2))