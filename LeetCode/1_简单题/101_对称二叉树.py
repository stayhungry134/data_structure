"""
name: 101_对称二叉树
create_time: 2023/9/7 19:34
author: Ethan

Description:  给你一个二叉树的根节点 root ， 检查它是否轴对称。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_symmetric(root: TreeNode) -> bool:
    def check(left: TreeNode, right: TreeNode) -> bool:
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return check(left.left, right.right) and check(left.right, right.left)

    return check(root.left, root.right)
