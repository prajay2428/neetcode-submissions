class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
            We are basically visiting every element in the grid and if we enocunter a 1 we increment number of islands, mark it as zero
            and mark all it's neighbours as zero in that way when we visit it's neighbours they will already have become zeroes so we
            don't have to increment the number of islands
        """
        rows = len(grid)
        columns = len(grid[0])
        num_of_islands = 0


        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= columns or grid[i][j] != "1":
                return

            else:
                grid[i][j] = "0"
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == "1":
                    num_of_islands += 1
                    dfs(i, j)

        return num_of_islands
