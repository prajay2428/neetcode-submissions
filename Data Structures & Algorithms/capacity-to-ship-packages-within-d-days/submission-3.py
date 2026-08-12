class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # min_weight should be max of wieghts because
        # if we pick a weight less than that then we can't
        # fit it in the ship
        # max weight will be sum of the weights because
        # if days are 1 then we should be able to fit all the weights
        # so min = max(weights) max = sum(weights)
        # between this range we need to do binary search
        def isEnough(ship_cap):
            # min_days it takes to fit all of the weights
            num_of_days = 1
            sum_weight = 0
            for weight in weights:
                sum_weight += weight
                if sum_weight > ship_cap:
                    sum_weight = weight
                    num_of_days += 1
            return num_of_days <= days
        
        lo = max(weights)
        hi = sum(weights)
        while lo < hi:
            mid = (lo+hi) // 2

            if isEnough(mid):
                hi = mid
            else:
                lo = mid + 1
        
        return lo




        