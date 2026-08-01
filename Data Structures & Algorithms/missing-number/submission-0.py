class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        remain = (1+n)*n/2
        for num in nums:
            remain -= num
        return int(remain)
