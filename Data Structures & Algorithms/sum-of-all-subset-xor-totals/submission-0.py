class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans,sol = [], []
        n = len(nums)

        def backtrack(i):
            if i == n:
                ans.append(sol[:])
                return
            
            backtrack(i+1)

            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
        
        backtrack(0)
        print(ans)
        xor= []
        for subset in ans:
            res = 0
            for element in subset:
                res ^= element
            
            xor.append(res)
        
        print(xor)
        return sum(xor)

            

        