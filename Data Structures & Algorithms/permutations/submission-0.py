class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans, sol = [], []
        n = len(nums)
        def backtrack():
            if len(sol) == n:
                ans.append(sol[:])
                return
            
            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backtrack()
                    sol.pop()
        
        backtrack()
        return ans
        