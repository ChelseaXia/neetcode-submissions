class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: # 处理边界条件，空网格
            return 0
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        def dfs(r, c):
            # 先判断终止条件
            if r<0 or c<0 or r >= rows or c >= cols or grid[r][c] == "0":
                return
            else:
                grid[r][c] = "0"
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c+1)
                dfs(r, c-1)
                
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    res += 1 # 在这里+1，不要在内层递归+1
                    dfs(r, c)
        return res
