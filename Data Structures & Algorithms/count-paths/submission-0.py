class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]

        print(dp)

        for i in range(n):
            dp[0][i] = 1
        
        for j in range(1,m):
            dp[j][0] = 1
        
        for r in range(1,m):
            for c in range(1,n):
                dp[r][c] = dp[r][c-1] + dp[r-1][c]
        
        print(dp)
        return dp[m-1][n-1]
        