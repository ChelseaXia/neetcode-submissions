class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i]表示抢到i的最多钱
        # 要么抢dp[i-1]，要么抢dp[i-2]
        n = len(nums)
        dp = [0] * (n+1)
        dp[1] = nums[0]
        for i in range(2, n+1):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
        return dp[n]