class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        return self.bisearch(target, nums, l, r)
    def bisearch(self, target, nums, l, r):
        # 把越界判断放在最前面，只要左边大于右边，肯定找不到
        if l > r:
            return -1
        mid = (l+r)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.bisearch(target, nums, mid+1, r)
        else:
            return self.bisearch(target, nums, l, mid-1)
            