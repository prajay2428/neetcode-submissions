class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def backtrack(i,total):
            if (i,total) in dp:
                return dp[(i,total)]
            if i >= len(nums):
                if total == target:
                    return 1
                
                else:
                    return 0
            
            left = backtrack(i+1,total+nums[i])
            right = backtrack(i+1,total-nums[i])
            dp[(i,total)] = left+right
            return left+right
        
        return backtrack(0,0)
        