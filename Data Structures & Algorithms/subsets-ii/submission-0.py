class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # 先排序
        res = []
        def dfs(path, start):
            res.append(path.copy())
            for i in range(start, len(nums)):
                # 不是当前层的第一个且和当前层之前的相同
                if i > start and nums[i] == nums[i-1]: # 如果是相同的，就跳过
                    continue
                path.append(nums[i])
                dfs(path, i+1)
                path.pop()
        dfs([], 0)
        return res
