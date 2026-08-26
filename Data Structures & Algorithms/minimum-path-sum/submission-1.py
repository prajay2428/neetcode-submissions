class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
       

        summ = 0 

        for r in range(rows):
            grid[r][0] = grid[r][0] + summ
            summ = grid[r][0]
        summ = 0    
        for c in range(0,cols):
            grid[0][c] = grid[0][c] + summ
            summ = grid[0][c]

        

        for r in range(1,rows):
            for c in range(1,cols):
                grid[r][c] = min(grid[r][c] + grid[r-1][c], grid[r][c] + grid[r][c-1])

        
        return grid[rows-1][cols-1]
        
        
        