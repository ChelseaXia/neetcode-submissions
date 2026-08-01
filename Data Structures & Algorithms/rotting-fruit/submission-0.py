class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 1. 用bfs，腐烂的橘子进队处理，数总共有多少个新鲜橘子
        # 2. 开始扩散腐烂，每一轮扩散时间+1
        # 3. 计算新鲜数是否减少到0
        m, n = len(grid), len(grid[0])
        rotten = deque()
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        minutes = 0
        while rotten and fresh > 0: # 这里条件要记得写fresh > 0
            minutes += 1
            for _ in range(len(rotten)): # 这里每一分钟需要把所有腐烂的橘子都处理完
                cur_x, cur_y = rotten.popleft()
                for (dx, dy) in [(1, 0), (0,1), (-1, 0), (0, -1)]:
                    if 0 <= cur_x+dx < m and 0 <= cur_y+dy< n and grid[cur_x+dx][cur_y+dy] == 1:
                        rotten.append((cur_x+dx, cur_y+dy))
                        grid[cur_x+dx][cur_y+dy] = 2
                        fresh -= 1
        return minutes if fresh == 0 else -1

                


        
        