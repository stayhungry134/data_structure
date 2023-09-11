"""
name: 94_二叉树的中序遍历
create_time: 2023/8/31 16:38
author: Ethan

Description: 给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root: Optional[TreeNode]) -> list[int]:
    """
    递归的方式实现
    刚开始使用递归的时候比较难以理解，不能够将一个问题化解为简单的逻辑
    可以把树设置为一颗一个根节点带左右叶子的树，然后去实现递归的逻辑代码
    """
    res = []

    def inorder(root: Optional[TreeNode]):
        if root is None:
            return res
        inorder(root.left)
        res.append(root.val)
        inorder(root.right)

    inorder(root)
    return res


def inorder_traversal1(root: Optional[TreeNode]) -> list[int]:
    """
    使用迭代的方式, 创建一个栈，然后先把左子树放进去，再把根节点放进去，最后把右节点放进去，依旧使用递归的思想
    :param root:
    :return:
    """
    tem = []
    res = []
    while root != None or len(tem) > 0:
        while root != None:
            tem.append(root.val)
            root = root.left
        current_val = tem.pop()
        res.append(current_val)
        root = root.right
    return res


def inorder_traversal2(root: Optional[TreeNode]) -> list[int]:
    # 先找到左子树最右边的节点
    # 把这个节点的右儿子改为根节点，然后把root给root的左儿子
    res = []
    if not root:
        return res
    while root is not None:
        if root.left is not None:
            rightmost = root.left
            while rightmost.right and rightmost.right != root:
                rightmost = rightmost.right
            # 如果rightmost 的右子树有东西，说明左边的已经访问完了
            if rightmost.right is not None:
                res.append(root.val)
                root = root.right
            # 如果右边还没有访问完
            else:
                rightmost.right = root
                root = root.left

        else:
            res.append(root.val)
            root = root.right
    return res
