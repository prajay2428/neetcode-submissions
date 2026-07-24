class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        perimeter = 0 

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] ==1:

                    for dr,dc in directions:
                        nr = dr + r
                        nc = dc + c

                        if nr <0 or nr >= rows or nc <0 or nc >=columns or grid[nr][nc] ==0:
                            perimeter += 1
                    
        return perimeter


        
                
                

        