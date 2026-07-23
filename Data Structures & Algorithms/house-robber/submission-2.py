class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        money = [0] * n # money代表经过这个房子可以拿到的最大金额
        if n == 0: return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        money[0] = nums[0]
        money[1] = max(money[0], nums[1])
        for i in range(2, n):
            money[i] = max(money[i-1],money[i-2]+nums[i]) # 要么这个房子抢，要么这个房子不抢
        return money[n-1]