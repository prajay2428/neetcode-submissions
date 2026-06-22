class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def s_works(num):
            l=1
            summ = 0

            for r in range(len(nums)):
                summ += nums[r]
                if summ > num:
                    l += 1
                    summ = nums[r]
            
            return l <= k
        # binary search

        lo = max(nums) # when k>=nums.length
        hi = sum(nums) # when k = 1

        while lo < hi:
            mid = (lo+hi) // 2

            if s_works(mid):
                hi = mid
            else:
                lo = mid+1

        return lo
        
            
           

        
        