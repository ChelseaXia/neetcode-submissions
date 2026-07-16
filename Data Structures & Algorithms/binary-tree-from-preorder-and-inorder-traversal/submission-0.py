# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 建立哈希映射
        idx = {v: i for i, v in enumerate(inorder)}
        def myBuildTree(pl, pr, il, ir):
            if pl > pr:
                return None
            cur = preorder[pl]
            root = TreeNode(cur)
            in_idx = idx[cur]
            len_left = in_idx-il
            root.left = myBuildTree(pl+1, pl+len_left, il, in_idx-1)
            root.right = myBuildTree(pl+len_left+1, pr, in_idx+1, ir)
            return root
        n = len(preorder)
        return myBuildTree(0, n-1, 0, n-1)
