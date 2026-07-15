# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 递归的方法
        # 对于某一个根节点，如果值合法（在最大最小值之间），继续判断左/右子树是否是valid
        # 递归终止条件：如果root不存在，那么return True
        def isValid(node, min_val=-float("inf"), max_val=float("inf")):
            if not node:
                return True
            if not (min_val<node.val<max_val):
                return False
            # 需要继承上一轮的最小值/最大值
            return isValid(node.left, min_val, node.val) and isValid(node.right, node.val, max_val)
        return isValid(root)
            
        