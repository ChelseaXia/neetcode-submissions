class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1) # 表示需要凑成这个数的最小完全平方数
        dp[0] = 0
        for i in range(1, n+1):
            j = 1 # 设置j的初始值
            while j*j <= n: # 通过while剪枝
                dp[i] = min(dp[i], dp[i-j*j]+1) # 递推公式
                j += 1 # j要记得+1
        return dp[n]
