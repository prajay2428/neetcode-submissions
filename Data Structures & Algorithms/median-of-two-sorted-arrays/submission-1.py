class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        final_nums = []
        n1 = len(nums1)
        n2 = len(nums2)
        k=0
        i=0
        j=0
        while k < n1+n2:

            if i==n1:

                final_nums.extend(nums2[j:])
                break
            
            if j==n2 :
                final_nums.extend(nums1[i:])
                break
            
            if nums1[i] <= nums2[j]:
                final_nums.append(nums1[i])
                i+=1
                k+=1
                
            
            elif nums2[j] <= nums1[i]:
                final_nums.append(nums2[j])
                j+=1
                k+=1
                


        if len(final_nums) % 2 == 0:
            mid = (0 + len(final_nums)-1) // 2
            median = (final_nums[mid] + final_nums[mid+1])/2
        
        else:
            mid = len(final_nums)//2
            median = final_nums[mid]
        
        return median

            

            


        