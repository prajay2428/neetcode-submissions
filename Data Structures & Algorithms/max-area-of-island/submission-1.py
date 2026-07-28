class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        max_area = 0

        def dfs(i,j):
            if i < 0 or i >= rows or j < 0 or j >= columns or grid[i][j] != 1:
                return 0
            
            grid[i][j] = 0
            area = 1
            area += dfs(i+1,j)
            area += dfs(i-1,j)
            area += dfs(i,j+1)
            area += dfs(i,j-1)
            
            return area
        

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    current_area = dfs(i,j)
                    max_area = max(max_area,current_area)
        
        return (max_area)
        