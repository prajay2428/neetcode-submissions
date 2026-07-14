import heapq
# we are implementing max heap
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.max_heap = [-n for n in nums]
        heapq.heapify(self.max_heap)
        
        
        

    def add(self, val: int) -> int:
        neg_val = -val
          
        heapq.heappush(self.max_heap,-val)
        arr = []
        for _ in range(self.k-1):
            num = heapq.heappop(self.max_heap)
            arr.append(num)
        ret = -self.max_heap[0]

        for num in arr:
            heapq.heappush(self.max_heap,num)

        return ret    

        
        
        
        
