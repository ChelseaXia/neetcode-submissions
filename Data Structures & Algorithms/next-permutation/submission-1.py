class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 从右往左遍历，找到第一个降序的
        n = len(nums)
        i = n-2
        # 这里要考虑i = 1的情况
        while i >= 0 and nums[i] >= nums[i+1]: 
            i -= 1 
        # 从右往左遍历，找到第一个比nums[i]大的nums[j]
        if i > 0: # 这里如果本身是最大排列的话就会跳过，因为i最后会等于-1
            for j in range(n-1, -1, -1):
                if nums[j] > nums[i]:
                    break
            # 交换位置
            nums[i], nums[j] = nums[j], nums[i]
        # 从i+1开始倒序
        l, r = i+1, n-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        

