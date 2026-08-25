class Solution:
    def numSquares(self, n: int) -> int:
        perfect_squares = []
        i =1
        while i**2 <= n:
            perfect_squares.append(i**2)
            i += 1
        
        dp = [1] * (n+1)
        dp[0] = 0

        for i in range(2,n+1):
            minn = float('inf')
            for square in perfect_squares:
                diff = i - square
                if diff < 0:
                    break
                minn = min(minn,1+dp[diff])
            
            dp[i] = minn
        
        print(dp)
        return dp[n]
                
                
         

        