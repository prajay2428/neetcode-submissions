class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return 0
        dp = [0]*n
        dp[1] = 1
        for i in range(2,n):
            minn = float('inf')
            for j in range(i):
                if j + nums[j] >= i:
                    minn = min(minn,dp[j]+1)
            dp[i] = minn
        
        return dp[n-1]
                
        