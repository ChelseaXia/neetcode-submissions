# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        # 开始交换左右子树
        tmp = root.left
        root.left = root.right
        root.right = tmp
        # 走一个递归
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root