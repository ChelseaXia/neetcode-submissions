class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # O(log(m+n))解法，把该矩阵当成一个array来做
        # 转换成对数组的二分搜索
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m*n-1
        while l <= r:
            mid = (l+r)//2
            row = mid//n
            col = mid%n
            cur = matrix[row][col]
            if cur == target:
                return True
            elif cur > target:
                r = mid-1
            elif cur < target:
                l = mid+1
        return False
        
