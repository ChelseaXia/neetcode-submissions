# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # 双重递归，先判断是否有大树
        # ok，判断大树下该节点和子树是否是同一颗树
        # 不是，继续搜索大树左右子树
        # 判断是否同一颗树就用之前的方法
        # 都没有就相同，一个有一个没或者值不相等就不同，如果值相同比较左右子树
        if not root:
            return False
        if self.isSametree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    def isSametree(self, p, q):
        if not p and not q:
            return True
        elif not p or not q or p.val != q.val:
            return False
        return self.isSametree(p.left, q.left) and self.isSametree(p.right, q.right)
