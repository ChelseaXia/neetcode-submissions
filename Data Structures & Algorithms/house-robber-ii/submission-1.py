class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        def linearrob(arr): # 有环打家劫舍，要么抢首不抢尾，要么不抢首抢尾，剩下和打家劫舍1一样
            prev, cur = 0, 0
            for num in arr:
                prev, cur = cur, max(cur, prev+num)
            return cur
        return max(linearrob(nums[1:]), linearrob(nums[:-1]))
