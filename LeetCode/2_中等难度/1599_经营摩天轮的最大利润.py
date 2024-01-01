"""
name: 
create_time: 2024/1/1 22:33
author: Ethan

Description: 你正在经营一座摩天轮，该摩天轮共有 4 个座舱 ，每个座舱 最多可以容纳 4 位游客 。你可以 逆时针 轮转座舱，但每次轮转都需要支付一定的运行成本 runningCost 。摩天轮每次轮转都恰好转动 1 / 4 周。

给你一个长度为 n 的数组 customers ， customers[i] 是在第 i 次轮转（下标从 0 开始）之前到达的新游客的数量。这也意味着你必须在新游客到来前轮转 i 次。每位游客在登上离地面最近的座舱前都会支付登舱成本 boardingCost ，一旦该座舱再次抵达地面，他们就会离开座舱结束游玩。

你可以随时停下摩天轮，即便是 在服务所有游客之前 。如果你决定停止运营摩天轮，为了保证所有游客安全着陆，将免费进行所有后续轮转 。注意，如果有超过 4 位游客在等摩天轮，那么只有 4 位游客可以登上摩天轮，其余的需要等待 下一次轮转 。

返回最大化利润所需执行的 最小轮转次数 。 如果不存在利润为正的方案，则返回 -1 。
"""


class Solution:
    def minOperationsMaxProfit(self, customers: list[int], boardingCost: int, runningCost: int) -> int:
        profit = [0]  # 利润列表
        surplus_customer = 0  # 剩余游客

        for customer in customers:
            # 将游客加到剩余游客中，然后在后续进行操作
            surplus_customer += customer
            # 如果顾客小于 4 个，那么直接坐摩天轮
            if customer < 4:
                current_profit = profit[-1] + customer * boardingCost - runningCost
                profit.append(current_profit)
            else:
                current_profit = profit[-1] + 4 * boardingCost - runningCost
                profit.append(current_profit)
                surplus_customer -= 4

        return profit.index(max(profit)) + 1


solution = Solution()

customers = [10, 9, 6]
boardingCost = 6
runningCost = 5

result = solution.minOperationsMaxProfit(customers, boardingCost, runningCost)

print(result)


