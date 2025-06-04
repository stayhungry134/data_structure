"""
name: lcp44_开幕式焰火
create_time: 2025/6/4 23:32
author: Ethan

Description: 
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def numColor(self, root: TreeNode) -> int:
        res = set()
        def dfs(node):
            if node is None:
                return
            res.add(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return len(res)

