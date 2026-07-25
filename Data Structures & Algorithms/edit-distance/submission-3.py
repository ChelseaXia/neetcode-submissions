class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp[i][j]代表截止到第一个字符串i位置和第二个字符串j位置时需要的改动点
        # 如果word1[i-1] == word2[j-1]
        # 啥也不用改，dp[i][j] = dp[i-1][j-1]
        # 如果word1[i-1] != word2[j-1]
        # 三种操作，增加一个，删除一个，改一个的最小改动字符数量
        # dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)
        m = len(word1)
        n = len(word2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        # 初始化边界条件
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # 分别是word1加一个字符，word1删一个字符，word1替换字符需要的改动量
                    dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)
        return dp[m][n]