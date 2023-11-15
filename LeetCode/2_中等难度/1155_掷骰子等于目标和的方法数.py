"""
name: 1155_掷骰子等于目标和的方法数
create_time: 2023/10/24 23:42
author: Ethan

Description: 这里有 n 个一样的骰子，每个骰子上都有 k 个面，分别标号为 1 到 k 。

给定三个整数 n ,  k 和 target ，返回可能的方式(从总共 kn 种方式中)滚动骰子的数量，使正面朝上的数字之和等于 target 。

答案可能很大，你需要对 109 + 7 取模 。
"""


class Solution:
    def __init__(self):
        self.result_mapping = {}

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        """

        :param n:
        :param k:
        :param target:
        :return:
        """
        return self.func(n, k, target) % (10 ** 7 + 9)

    def func(self, n, k, target):
        if n == 0:
            return 0
        # 如果骰子数大于目标值，返回0
        if n > target or n * k <= target:
            return 0
        # 如果只有一个骰子并且目标值小于骰子面数，返回1
        if n == 1:
            return 1 if 1 <= target <= k else 0
        # 字典中存在目标值，就直接返回
        tem_result = self.result_mapping.get(f"{n}-{target}")
        if tem_result:
            return tem_result
        else:
            pre_target = target - min(k, target)
            pre_result = self.func(n - 1, k, pre_target)

            return pre_result * min(k, pre_target)


solution = Solution()
print(solution.numRollsToTarget(2, 6, 7))


def numRollsToTarget(n, k, target):
    MOD = 10**9 + 7
    # 初始化二维动态规划数组
    dp = [[0] * (target + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            for x in range(1, min(j, k) + 1):
                dp[i][j] = (dp[i][j] + dp[i - 1][j - x]) % MOD

    return dp[n][target]

n = 3
k = 6
target = 13
result = numRollsToTarget(n, k, target)
print(result)

