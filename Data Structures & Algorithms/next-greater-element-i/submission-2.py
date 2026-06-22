class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stk = []
        hashmap={}
        ans = []

        for num in nums2:
            if not stk:
                stk.append(num)
                continue
            if stk[-1] > num:
                stk.append(num)
            
            else:
                while stk and stk[-1] < num :
                    hashmap[stk[-1]] = num
                    stk.pop()

                stk.append(num)
        if stk:
            for num in stk:
                hashmap[num] = -1
        
        for num in nums1:
            ans.append(hashmap[num])
        return ans


                
            

        