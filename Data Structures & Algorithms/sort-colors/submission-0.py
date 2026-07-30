class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        r, b = 0, n-1
        i = 0
        while i<n and r <= i <= b:
            if nums[i] == 0:
                nums[r], nums[i] = nums[i], nums[r]
                r += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                nums[i], nums[b] = nums[b], nums[i]
                b -= 1
        

