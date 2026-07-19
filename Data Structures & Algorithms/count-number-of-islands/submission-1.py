class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS版本，用队列来做
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        ans = 0
        def bfs(r, c):
            queue = deque()
            queue.append((r, c)) # 加入队列
            grid[r][c] = '0'
            while queue:
                r, c = queue.popleft() # 弹出该点
                for dr, dc in ([-1, 0], [1, 0], [0, -1], [0, 1]):
                    next_r, next_c = r+dr, c+dc
                    if (0 <= next_r < rows) and (0 <= next_c < cols) and grid[next_r][next_c] == '1':
                        grid[next_r][next_c] = '0'
                        queue.append((next_r, next_c)) # 把下一个点也加进队列
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    bfs(r, c)
                    ans += 1   
        return ans                     

        