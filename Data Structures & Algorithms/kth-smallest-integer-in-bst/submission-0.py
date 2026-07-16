# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 中序遍历：左-根-右
        # 用循环的方式来做，想到栈
        count = 0
        cur = root
        stack = []
        # 循环存在的条件：要么当前节点有值，要么节点为null但是栈不空
        while cur or stack: 
            while cur:
                stack.append(cur)
                cur = cur.left
            now = stack.pop()
            count += 1
            if count == k:
                return now.val
            cur = now.right # 继续访问右边的子节点
        
