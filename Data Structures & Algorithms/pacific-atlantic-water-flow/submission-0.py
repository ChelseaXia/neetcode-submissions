class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        rows, cols = len(heights), len(heights[0])
        pacific = [[False] * cols for _ in range(rows)]
        atlantic = [[False] * cols for _ in range(rows)]
        def dfs(r, c, ocean, prev_height):
            # 先判断是否越界或者不符合条件
            if r >= rows or r < 0 or c >= cols or c < 0 or ocean[r][c] or heights[r][c] < prev_height:
                return 
            ocean[r][c] = True
            dfs(r+1, c, ocean, heights[r][c])
            dfs(r-1, c, ocean, heights[r][c])
            dfs(r, c+1, ocean, heights[r][c])
            dfs(r, c-1, ocean, heights[r][c])
        for c in range(cols):
            dfs(0,c,pacific,0)
            dfs(rows-1,c,atlantic,0)
        for r in range(rows):
            dfs(r,0,pacific,0)
            dfs(r,cols-1,atlantic,0)
        res = []
        for r in range(rows):
            for c in range(cols):
                if pacific[r][c] and atlantic[r][c]:
                    res.append([r,c])
        return res
            
            