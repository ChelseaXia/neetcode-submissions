class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 记录以当前num为最后一个数的最大和
        max_sum = -float("inf")
        n = len(nums)
        pre_sum = [-float("inf")] * (n+1)
        for i in range(1, n+1):
            pre_sum[i] = max(pre_sum[i-1]+nums[i-1], nums[i-1])
            max_sum = max(max_sum, pre_sum[i])
        return max_sum
