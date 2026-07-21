class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res,sol = [],[]
        nums = candidates
        nums.sort()
        n = len(nums)
        def backtrack(i,cur_sum):
            if cur_sum == target:
                if sol[:] not in res:
                    res.append(sol[:])
            
            if cur_sum > target or i ==n:
                return 
            
            
            

            sol.append(nums[i])
            backtrack(i+1,cur_sum+nums[i])
            sol.pop()


            while i+1 < n and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1,cur_sum)
        
        backtrack(0,0)
        print(res)
        return res
        