class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t : t[1])
        minHeap = [] #[end,numPass]
        currPass = 0

        for t in trips:
            numPass,start,end = t

            while minHeap and minHeap[0][0] <=start:
                passengers = heapq.heappop(minHeap)[1]
                currPass -= passengers
            
            currPass += numPass
            if currPass > capacity:
                return False
            
            heapq.heappush(minHeap,[end,numPass])
        
        return True
        