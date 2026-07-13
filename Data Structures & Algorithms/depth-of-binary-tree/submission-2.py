# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # BFS，用双端队列来处理
        if not root:
            return 0
        queue = deque([root])
        depth = 0 # 初始化深度为0
        while queue:
            level_size = len(queue) # 确定这一层有多少个节点
            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1 # 这一层处理完了，depth ++
        return depth