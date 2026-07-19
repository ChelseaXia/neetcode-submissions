class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        length = len(word)
        def dfs(r, c, k):
            # 成功条件
            if k == length: # 注意这里是单词长度，因为前面所有都匹配完了
                return True
            # 失败条件
            if (r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[k]):
                return False
            temp = board[r][c]
            board[r][c] = '#'
            res = (dfs(r+1, c, k+1) or
                    dfs(r, c+1, k+1) or
                    dfs(r-1, c, k+1) or
                    dfs(r, c-1, k+1))
            # 恢复原样
            board[r][c] = temp
            return res
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False