class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        frequency=[0]*2

        left=0
        max_length=0

        for right in range(len(nums)):
            frequency[nums[right]]+=1
            while (right-left+1) - frequency[1] > k:
                
                frequency[nums[left]] -= 1
                left +=1
            
            max_length = max(max_length,right-left+1)

        return max_length
        