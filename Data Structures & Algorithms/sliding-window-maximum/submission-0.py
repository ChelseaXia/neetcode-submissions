class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k > n:
            return max(nums)
        l, r = 0, k-1
        res = (n-k+1) * [0]
        while r < n:
            res[l] = max(nums[l:r+1])
            l += 1
            r += 1
        return res