import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
            [2,3,6,2,4]
        """
        if len(stones) == 1:
            return stones[0]
        if len(stones) ==0:
            return 0
        for i in range(len(stones)):
            stones[i] = -stones[i]
        
        
        heapq.heapify(stones)
        

        while True:
            
            heaviest = -heapq.heappop(stones)
            second_heaviest = -heapq.heappop(stones)
            print(heaviest,second_heaviest)
            
            if heaviest > second_heaviest:
                remainder = -(heaviest - second_heaviest)
                heapq.heappush(stones,remainder)
                if len(stones) ==1:
                    break 
            if heaviest == second_heaviest and len(stones) == 0:
                return 0  
            if len(stones) ==1:
                break
            

        return -stones[0] if len(stones) == 1 else 0  


            

        