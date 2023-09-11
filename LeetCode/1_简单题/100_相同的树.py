"""
name: 100_相同的树
create_time: 2023/9/3 20:45
author: Ethan

Description: 给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p == q is None:
        return True
    if p and q:
        if p.val != q.val:
            return False
    try:
        return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
    except:
        return False
