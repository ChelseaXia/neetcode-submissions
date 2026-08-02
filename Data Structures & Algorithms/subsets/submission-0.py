class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(start, path):
            res.append(path.copy()) # 每一个子集都是合法元素
            for i in range(start, len(nums)): # 注意要从start开始
                path.append(nums[i])
                dfs(i+1, path) # 注意传的是i
                path.pop()
        dfs(0, [])
        return res
