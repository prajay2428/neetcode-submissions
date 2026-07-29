class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        queue = deque()
        seen = set()

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 2:
                    queue.append([i, j])
                    seen.add((i, j))
        minutes = 0
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        while queue:
            size = len(queue)
            for _ in range(size):
                r, c = queue.popleft()
                for nr, nc in directions:
                    dr = nr + r
                    dc = nc + c
                    if (
                        dr < 0
                        or dr >= rows
                        or dc < 0
                        or dc >= columns
                        or grid[dr][dc] == 0
                        or grid[dr][dc] == 2
                    ):
                        continue
                    else:
                        grid[dr][dc] = 2
                        queue.append([dr, dc])
            if queue:
                minutes += 1
        for row in grid:
            if 1 in row:
                return -1

        return minutes
