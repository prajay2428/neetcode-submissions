class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        

        for num in nums1:
            greater_element = -1
            idx = nums2.index(num)
            for i in range(idx+1,len(nums2)):
                if nums2[i] > num:
                    greater_element = nums2[i]
                    break

            ans.append(greater_element)
        return ans
        