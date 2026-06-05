class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        longest=0
        s=set(nums)

        for num in nums:
           if num-1 not in s:

            next_num=num+1
            length=1
            while next_num in s:
                length+=1
                next_num+=1
            longest=max(length,longest)
        return longest
        