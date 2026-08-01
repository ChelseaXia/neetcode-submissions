class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n): # 参考缺失的正数的方法
            while nums[i] != i and nums[i] < n:
                target_idx = nums[i]
                nums[target_idx], nums[i] = nums[i], nums[target_idx]
        for i in range(n):
            if nums[i] != i:
                return i
        return n
