"""
name: 121_买卖股票的最佳时机
create_time: 2023/9/4 16:11
author: Ethan

Description: 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0
"""


def max_profit(prices: list[int]) -> int:
    if not prices:
        return 0
    min_price = prices[0]
    res = 0
    for price in prices:
        if price < min_price:
            min_price = price
        res = max(price - min_price, res)
    return res


ls = [7, 1, 5, 3, 6, 4]
print(max_profit(ls))
