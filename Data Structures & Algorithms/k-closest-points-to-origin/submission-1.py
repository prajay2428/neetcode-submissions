import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        distances=[]
        for point in points:
            x,y = point
            distance = math.sqrt(x**2 + y**2)
                # distances.append(distance)
            heapq.heappush(heap,(distance,point))
            if len(heap) > k:
                heapq.heappop
        
        ans = []

        for _ in range(k):
            dist,point = heapq.heappop(heap)
            ans.append(point)

        return ans
            

        
        
        