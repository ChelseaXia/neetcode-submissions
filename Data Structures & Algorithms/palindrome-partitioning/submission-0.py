class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # 先预处理，dp[i][j]存储s[i:j+1]是否是回文
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j-i <= 1 or dp[i+1][j-1]): # 需要考虑子串长度小于等于2的情况
                    dp[i][j] = True
        
        res = []
        path = []
        def dfs(start):
            if start == n:
                res.append(path.copy())
                return
            for i in range(start, n):
                if dp[start][i]: # 如果是回文
                    path.append(s[start:i+1]) # 添加
                    dfs(i+1)
                    path.pop()
        dfs(0)
        return res
