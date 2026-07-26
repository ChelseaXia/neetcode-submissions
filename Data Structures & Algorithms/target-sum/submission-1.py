class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 考虑用dfs做
        # 要么+，要么-
        n = len(nums)
        def dfs(cur_sum, i):
            if i == n:
                if cur_sum == target: return 1
                else: return 0
            return dfs(cur_sum+nums[i], i+1)+dfs(cur_sum-nums[i], i+1)
        return dfs(0, 0)