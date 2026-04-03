class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        INF = 2147483647
        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i,j))
        

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            r,c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr<0 or nr >= rows or nc < 0 or nc >= cols:
                    continue
                
                if grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr,nc))


