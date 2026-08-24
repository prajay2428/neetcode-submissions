class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] *(2*n)
        # base case
        dp[0], dp[1] = nums[0], nums[0]
        for i in range(1,n):
            dp[2*i] = min(nums[i],nums[i]*dp[2*i-2],nums[i]*dp[2*i-1])
            dp[2*i+1] = max(nums[i],nums[i]*dp[2*i-2],nums[i]*dp[2*i-1])
        
        return max(dp)
        