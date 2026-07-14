import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
            [2,3,6,2,4]
        """
        
        for i in range(len(stones)):
            stones[i] = -stones[i]
        
        
        heapq.heapify(stones)
        

        while len(stones) >= 2:
            heaviest = -heapq.heappop(stones)
            second_heaviest = -heapq.heappop(stones)

            if heaviest > second_heaviest:
                remainder = heaviest - second_heaviest
                heapq.heappush(stones,-remainder)
            
        if len(stones) == 1:
            return -stones[0]
        else:
            return 0



            

        