class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 核心思想，把1~N的每个数都放到自己应该在的位置上，只要有不在的那么缺的就是这个数
        n = len(nums)
        for i in range(n):
            # 注意这里要用while，因为换过来的数也不一定在正确的位置上！
            while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
                target_idx = nums[i]-1
                nums[target_idx], nums[i] = nums[i], nums[target_idx]
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n+1