class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        # 先去有序的那一边确定，不在就去无序那里找
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[l]: # 说明左边有序，这里记得要加等号！
                if target >= nums[l] and target < nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            else: # 右边有序
                # 去右边看看在不在
                if target > nums[mid] and target <= nums[r]:
                    l = mid+1
                # 不在，去左边碰运气
                else:
                    r = mid-1
        return -1
