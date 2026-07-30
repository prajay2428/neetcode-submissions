class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # check all the border 'O's and from there check if you can reach
        # other 'O's, if you can reach them, mark them as 's' or anything
        # after that go through the grid mark all 's' as 'O' and remaining ones
        # as 'X'
        border = []

        rows, columns = len(board),len(board[0])

        
        for i in range(rows):
            border.append((i, 0))
            border.append((i, columns - 1))

        
        for j in range(1, columns - 1):
            border.append((0, j))
            border.append((rows - 1, j))

        def dfs(i,j):
            if i < 0 or i >= rows or j < 0 or j >= columns or board[i][j] == 'X' or board[i][j] =='S':
                return
            board[i][j] = 'S'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            
            return 
            
            
        
        for i,j in border:
            if board[i][j] == 'O':
                dfs(i,j)
        print(board)
        
        for i in range(rows):
            for j in range(columns):
                if board[i][j] == 'S':
                    board[i][j] = 'O'
                
                elif board[i][j] == 'O':
                    board[i][j] ='X'
            
            