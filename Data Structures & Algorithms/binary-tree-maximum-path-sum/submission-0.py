# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = -float("inf")
        def node_max(node):
            if not node:
                return 0
            left_max = max(node_max(node.left), 0)
            right_max = max(node_max(node.right), 0)
            cur_max = left_max + right_max + node.val
            self.max_sum = max(self.max_sum, cur_max)

            return node.val + max(left_max, right_max)
        node_max(root)
        return self.max_sum
