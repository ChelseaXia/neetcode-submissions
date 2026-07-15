# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: # 前置空节点判断一定要有
            return []       
        queue = deque([root]) # 在这里把根节点加进去
        res = []
        while queue:
            ans = [] # 需要重新初始化一个空列表
            # 这里用队列大小指示这一层有多少节点
            level_size = len(queue)
            for _ in range(level_size):
                cur = queue.popleft()
                ans.append(cur.val)
                # 这里要注意只有不为空才会入队
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(ans)
        return res
            
            