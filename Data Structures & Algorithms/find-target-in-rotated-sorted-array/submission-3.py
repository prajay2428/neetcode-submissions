class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l < r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            elif nums[l] == target:
                return l
            elif nums[r] == target:
                return r
                
            elif nums[mid] > nums[r] and target < nums[r]:
                l = mid + 1
            
            elif nums[mid] < nums[r] and target < nums[r]:
                if target < nums[mid]:
                    r = mid - 1
                
                else:
                    l = mid + 1
            
            elif nums[mid] > nums[r] and target > nums[r]:
                if target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            
            elif nums[mid] < nums[r] and target > nums[r]:
                r = mid - 1

                
            
            
        if nums[l] == target:
            return l
        else:
            return -1
                
                                                                             
        