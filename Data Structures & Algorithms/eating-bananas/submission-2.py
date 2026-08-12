class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # min rate = min of array 
        # max rate = max of array
        def isEatable(rate):
            num_of_hours = 0
            for pile in piles:
                num_of_hours += math.ceil(pile/rate)
                if num_of_hours > h:
                    return False
            
            return True
        
        lo = 1
        hi = max(piles)

        while lo < hi:
            mid = (lo + hi) // 2

            if isEatable(mid):
                hi = mid
            else:
                lo = mid+1
        
        return lo


        
        