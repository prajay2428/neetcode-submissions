class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,columns = len(grid),len(grid[0])
        queue = deque()
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        seen = set()

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] ==0:
                    queue.append([i,j])
                    seen.add((i,j))
        
        while queue:
            size = len(queue)
            for _ in range(size):
                r,c = queue.popleft()
                for nr,nc in directions:
                    dr = nr+r
                    dc = nc+c
                    if dr <0 or dr>=rows or dc<0 or dc>=columns or grid[dr][dc] == -1 or (dr,dc) in seen:
                        continue
                    else:
                        grid[dr][dc] = grid[r][c] + 1
                        queue.append([dr,dc])
                        seen.add((dr,dc))
        
        
        