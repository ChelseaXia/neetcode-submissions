class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        flags = [0] * len(nums)
        def dfs(path, idx):
            if idx == len(nums):
                res.append(path.copy())
                return
            for i, num in enumerate(nums):
                if flags[i] == 0:
                    path.append(num)
                    flags[i] = 1
                    dfs(path, idx+1)
                    path.pop()
                    flags[i] = 0
            return
        dfs([], 0)
        return res