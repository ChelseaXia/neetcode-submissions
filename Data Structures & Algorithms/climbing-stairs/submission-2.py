class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[i]代表当前有多少种方式
        # dp[i] = dp[i-1]+dp[i-2]
        dp = [1] * (n+1)
        for i in range(2, n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]