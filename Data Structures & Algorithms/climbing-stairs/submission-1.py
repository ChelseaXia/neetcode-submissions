class Solution:
    def climbStairs(self, n: int) -> int:
        # 动态规划
        # 要爬到最顶上，从前一级出发有1种方式，从前2级出发也有1种方式
        # 滚动更新的方法
        if n<=2:
            return n
        a, b = 1, 2
        for _ in range(3, n+1): # a 代表 dp[i-2]，b 代表 dp[i-1]
            a, b = b, a+b
        return b