# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 二叉搜索树（BST），通过大小关系（左全部<中<右全部）剪枝
        # 如果全都小于root说明祖先在左边，如果全都大于root说明祖先在右边
        # 其他情况说明这个就是祖先
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root