class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 算从某个头开始的乘积max的subarray
        # dp存以某个位置结尾的乘积max/min
        # 这样下一个元素进来的时候只需要判断是否要和上一个的max或者min相乘就行
        n = len(nums)
        max_dp = [-float('inf')] * (n+1)
        min_dp = [float('inf')] * (n+1)
        max_dp[0] = 1
        min_dp[0] = 1
        max_p = -float('inf')
        for i in range(1, n+1):
            # 最大值只能从3个里面产生，上一个最大值和这个相乘，上一个最小值和这个相乘，这个值
            max_dp[i] = max(min_dp[i-1]*nums[i-1], max_dp[i-1]*nums[i-1], nums[i-1])
            min_dp[i] = min(min_dp[i-1]*nums[i-1], max_dp[i-1]*nums[i-1], nums[i-1])
            max_p = max(max_p, max_dp[i])
        return max_p


