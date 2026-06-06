class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # for i in range(len(nums)):

        #     for j in range(i+1,len(nums)):
                
        #         if nums[i] == nums[j]:
                    
        #             if abs(i-j)<=k:

        #                 return True
                    
        # return False
        seen={}
        for i in range(len(nums)):
            
            
            if nums[i] not in seen:
                seen[nums[i]]=i
                

            elif nums[i] in seen:
                if abs(seen[nums[i]]-i) <=k:
                    return True
                else:
                    seen[nums[i]]=i
                
        return False
                


        
        