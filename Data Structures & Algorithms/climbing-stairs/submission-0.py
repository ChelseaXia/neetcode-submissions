class Solution:
    def climbStairs(self, n: int) -> int:
        # 动态规划
        # 要爬到最顶上，从前一级出发有1种方式，从前2级出发也有1种方式
        if n<=2: # 考虑边界条件
            return n
        dp = [0]*(n+1)
        dp[1]=1
        dp[2]=2
        for i in range(3, n+1): # 从3开始
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]