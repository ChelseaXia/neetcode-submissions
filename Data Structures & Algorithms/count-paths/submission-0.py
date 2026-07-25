class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1]*n
        # 用一维dp简化空间
        # 每一行滚动更新，到达当前点的数量=左边一个+上面一格的数量
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        return dp[n-1]