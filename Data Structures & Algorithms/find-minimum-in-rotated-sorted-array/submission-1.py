class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        min = nums[r]
        while l < r:
            mid = (l+r)//2
            # 总是与右边的比较，rotate后会有两段升序，只有两种可能
            # mid比r大，min在[mid+1,r]
            # mid比r小，min在[l, mid]
            if nums[mid] > nums[r]:
                l = mid+1
            elif nums[mid] < nums[r]:
                r = mid
        return nums[l]


