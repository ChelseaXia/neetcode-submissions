class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) # m行
        n = len(matrix[0]) # n列
        for r in range(m):
            if target == matrix[r][n-1]:
                return True
            elif target > matrix[r][n-1]:
                continue
            elif target < matrix[r][n-1]:
                return self.bisearch(matrix[r], target, 0, n-2)
        return False
    
    def bisearch(self, nums, target, l, r):
        if l > r:
            return False
        mid = (l+r)//2
        if nums[mid] == target:
            return True
        elif nums[mid] > target:
            return self.bisearch(nums, target, l, mid-1)
        else:
            return self.bisearch(nums, target, mid+1, r)