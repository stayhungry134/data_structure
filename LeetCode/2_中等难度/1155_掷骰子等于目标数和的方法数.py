"""
name: 1155_掷骰子等于目标数和的方法数
create_time: 2023/10/24 17:37
author: Ethan

Description: 这里有 n 个一样的骰子，每个骰子上都有 k 个面，分别标号为 1 到 k 。

给定三个整数 n ,  k 和 target ，返回可能的方式(从总共 kn 种方式中)滚动骰子的数量，使正面朝上的数字之和等于 target 。

答案可能很大，你需要对 109 + 7 取模 。
"""


class Solution:
    def __init__(self):
        self.result_map = {}
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        """
        求解掷骰子等于目标数和的方法数
        :param n: n 个骰子
        :param k: 每个骰子可能的面数，看出现从 1 到 k
        :param target: 最后要达到的目标和数
        :return: 返回目标和数
        """
        return self.func(n, k, target) % (10 ^ 9 + 7)

    def func(self, n: int, k: int, target: int) -> int:
        # 如果目标数比骰子数还小，返回0
        if target < n:
            return 0
        # 如果只有一个骰子，并且target在骰子可能范围只能，那么只有一种情况
        if n == 1 and target < k:
            return 1
        # 如果值已经记录，那么直接返回
        tem_result = self.result_map.get(f'n-{target}')
        if tem_result:
            return tem_result
        else:
            pre_target = min(target, k)
            pre_result = self.numRollsToTarget(n - 1, k, target - pre_target)
            self.result_map[f'{n-1}-{pre_target}'] = pre_result
            return pre_result * min(target, k)


solution = Solution()
print(solution.numRollsToTarget(30, 30, 500))