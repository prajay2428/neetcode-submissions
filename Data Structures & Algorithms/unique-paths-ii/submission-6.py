class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        

        for r in range(rows):
            for c in range(cols):
                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = 'X'
        

        for r in range(rows):
            if obstacleGrid[r][0] == 'X':
                break
            
            obstacleGrid[r][0] = 1
        
        for c in range(cols):
            if obstacleGrid[0][c] == 'X':
                break
            
            obstacleGrid[0][c] = 1
    
         
            
        
        
        

        for r in range(1,rows):
            for c in range(1,cols):
                if obstacleGrid[r][c] == 'X':
                    continue

                left = obstacleGrid[r][c-1]
                top = obstacleGrid[r-1][c]
                if obstacleGrid[r][c-1] =='X':
                    left = 0
                if obstacleGrid[r-1][c] == 'X':
                    top = 0
                
                obstacleGrid[r][c] = top + left
        

        return 0 if obstacleGrid[rows-1][cols-1] == 'X' else obstacleGrid[rows-1][cols-1]
            
        