class TrieNode():
    def __init__(self):
        self.children = {}
        self.word = ""

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 1. 建树
        root = TrieNode()
        for w in words:
            node = root
            for c in w:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.word = w
        # 2. 网格和树同步做dfs
        rows, cols = len(board), len(board[0])
        res = set()
        def dfs(r, c, node):
            # 失败出口：越界or当前字母在前缀树下一个步不存在
            if r<0 or c<0 or r>=rows or c>=cols or board[r][c] not in node.children:
                return
            char = board[r][c]
            next_node = node.children[char]

            if next_node.word != "":
                res.add(next_node.word)
            
            board[r][c] = '#'

            dfs(r+1, c, next_node)
            dfs(r-1, c, next_node)
            dfs(r, c+1, next_node)
            dfs(r, c-1, next_node)

            board[r][c] = char
        
        # 3. 主循环
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        return list(res)