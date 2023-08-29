"""
name: 1443_收集书上所有苹果的最少时间
create_time: 2023/7/2 23:34
author: Ethan

Description: 给你一棵有 n 个节点的无向树，节点编号为 0 到 n-1 ，它们中有一些节点有苹果。通过树上的一条边，需要花费 1 秒钟。你从 节点 0 出发，请你返回最少需要多少秒，可以收集到所有苹果，并回到节点 0 。

无向树的边由 edges 给出，其中 edges[i] = [from i, to i] ，表示有一条边连接 from 和 toi 。除此以外，还有一个布尔数组 hasApple ，其中 hasApple[i] = true 代表节点 i 有一个苹果，否则，节点 i 没有苹果。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/minimum-time-to-collect-all-apples-in-a-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def min_time(n: int, edges: list[list[int]], has_apple: list[bool]) -> int:
    result = 0
    index = 0
    while index < len(edges):
        if has_apple[index] == True:
            result += 2
        index