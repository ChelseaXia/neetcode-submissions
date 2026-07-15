# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 写一个最普通树的LCA
        # 递归
        # 最底层边界条件/递归出口是什么？空，或者找到了p/q
        if not root or root.val == p.val or root.val == q.val:
            return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        # 左右子树各发现一个节点
        if l and r:
            return root
        # 发现啥返回啥
        return l if l else r
        