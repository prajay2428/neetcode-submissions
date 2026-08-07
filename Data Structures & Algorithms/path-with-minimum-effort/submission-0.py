class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows,columns = len(heights),len(heights[0])

        heap = [[0,0,0]]
        seen = set()
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        while heap:
            diff, r, c = heapq.heappop(heap)

            if (r,c) in seen:
                continue
            if (r,c) == (rows-1,columns-1):
                return diff
            seen.add((r,c))

            for dr,dc in directions:
                nr,nc = dr+r,dc+c
                if (nr<0 or nc< 0 or nr>=rows or nc>=columns or (nr,nc) in seen):
                    continue
                new_diff = max(abs(heights[r][c] - heights[nr][nc]),diff)
                heapq.heappush(heap,[new_diff,nr,nc])


            

        
        

        
            


        