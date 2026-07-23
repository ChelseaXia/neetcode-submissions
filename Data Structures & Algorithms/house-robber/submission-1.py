class Solution:
    def rob(self, nums: List[int]) -> int:
        # 对每一个House只有rob和不rob两个选择
        # 之前的状态是rob，那么这个就不rob
        # 之前的状态不rob，那么这个就rob
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
            money[i] = max(money[i-1],money[i-2]+nums[i])
        return money[n-1]