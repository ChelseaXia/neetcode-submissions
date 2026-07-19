class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 回溯法
        # 先排序，方便后续剪枝
        res = []
        nums.sort()
        def backtracking(remain, start, path):   
            if remain == 0: # 满足条件
                res.append(list(path)) # 要么套一层list要么给一个copy
                return
            # 不满足就继续遍历
            for i in range(start, len(nums)): # 这里要传start防止重新看过去的数字
                if nums[i] > remain:
                    break # 剪枝
                path.append(nums[i])
                # 注意可以重复使用，所以start还是i
                backtracking(remain-nums[i], i, path)
                path.pop()
        backtracking(target, 0, [])
        return res
                
