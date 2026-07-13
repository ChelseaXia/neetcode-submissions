# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # BFS解法
        queue = deque([(p, q)]) # 注意这里的写法，中括号里面是圆括号，因为要传一对连体的元组进去
        while queue:
            node_p, node_q = queue.popleft()
            if not node_p and not node_q:
                continue
            if not node_p or not node_q or (node_p.val != node_q.val):
                return False
            queue.append((node_p.left, node_q.left)) # 注意，这里直接传一个元组就行，不需要加中括号
            queue.append((node_p.right, node_q.right))
        return True
        