class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        # 考虑先做前缀积，再做后缀积
        pre = 1
        for i in range(n):
            res[i] *= pre
            pre *= nums[i]
        
        post = 1
        for i in range(n-1, -1, -1):
            res[i] *= post
            post *= nums[i]
        
        return res
