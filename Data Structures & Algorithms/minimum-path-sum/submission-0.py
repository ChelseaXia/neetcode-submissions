class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 对于每一个位置，它的最小路径和都是
        # grid[i][j] + min左边的位置/min右边的位置 的sum
        m = len(grid)
        n = len(grid[0])
        min_sum = [[float('inf')] * (n+1) for _ in range(m+1)]
        min_sum[0][0] = min_sum[1][0] = min_sum[0][1] = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                min_sum[i][j] = grid[i-1][j-1] + min(min_sum[i-1][j], min_sum[i][j-1])
        return min_sum[m][n]