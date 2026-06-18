class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        ans = 0 
        lo = 1
        hi = x //2 

        while lo <= hi:
            mid = (lo + hi) // 2

            res = mid * mid

            if res == x:
                return mid 
            
            elif res < x:
                ans = mid 
                lo = mid + 1
            
            else:
                hi = mid - 1

            
        return ans
        