# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        # 将一棵二叉树化为字符串
        # 用前序遍历的方式做
        def dfs(node):
            if not node:
                res.append("#")
                return
            # 先处理根节点
            res.append(str(node.val))
            # 处理左叶子
            dfs(node.left)
            # 处理右叶子
            dfs(node.right)
        dfs(root)
        return ' '.join(res) # 用空格相隔，逗号也行
    
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(' ') # 先把字符串拆开
        # 引入一个迭代器
        iter_vals = iter(vals)
        def dfs():
            vals = next(iter_vals) # 迭代器的用法：next(迭代器）就能取出下一个值
            if vals == '#': # 发现是空节点
                return None
            node = TreeNode(int(vals))
            node.left = dfs()
            node.right = dfs()
            return node
        root = dfs()
        return root


