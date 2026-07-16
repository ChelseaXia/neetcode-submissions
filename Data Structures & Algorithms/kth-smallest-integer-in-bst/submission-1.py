# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 用遍历的方法去做
        self.k = k # 用类把k存起来
        self.ans = None
        def dfs(node):
            if not node:
                return

            dfs(node.left)
            # 处理根节点
            self.k -= 1
            if self.k == 0:
                self.ans = node.val
                return # 找到了，提前结束
                
            dfs(node.right)
            
        dfs(root)
        return self.ans
