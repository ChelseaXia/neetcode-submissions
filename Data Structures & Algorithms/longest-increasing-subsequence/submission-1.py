class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 动态规划解法
        # dp存以这个为最后一个数字的最长递增数组长度
        n = len(nums)
        dp = [1]*n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j]+1, dp[i])
        return max(dp)