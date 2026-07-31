class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 实际rotate的次数r = k % n
        n = len(nums)
        r = k%n
        # 三次翻转法
        # 1. 整体翻转
        def rotate(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        rotate(0, n-1)
        rotate(0, r-1)
        rotate(r, n-1)
