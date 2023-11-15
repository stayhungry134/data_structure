"""
name: 1333_餐厅过滤器
create_time: 2023/9/27 15:41
author: Ethan

Description: 给你一个餐馆信息数组 restaurants，其中  restaurants[i] = [idi, ratingi, veganFriendlyi, pricei, distancei]。你必须使用以下三个过滤器来过滤这些餐馆信息。

其中素食者友好过滤器 veganFriendly 的值可以为 true 或者 false，如果为 true 就意味着你应该只包括 veganFriendlyi 为 true 的餐馆，为 false 则意味着可以包括任何餐馆。此外，我们还有最大价格 maxPrice 和最大距离 maxDistance 两个过滤器，它们分别考虑餐厅的价格因素和距离因素的最大值。

过滤后返回餐馆的 id，按照 rating 从高到低排序。如果 rating 相同，那么按 id 从高到低排序。简单起见， veganFriendlyi 和 veganFriendly 为 true 时取值为 1，为 false 时，取值为 0 。
"""

class Solution:
    def filterRestaurants(self, restaurants: list[list[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> list[int]:
        standard_restaurants = [restaurant for restaurant in restaurants if restaurant[3] < maxPrice and restaurant[4] < maxDistance]
        if veganFriendly == 1:
            standard_restaurants = [restaurant for restaurant in standard_restaurants if restaurant[2] == 1]

    def merge_sort(self, restaurants):
        res_len = len(restaurants)


