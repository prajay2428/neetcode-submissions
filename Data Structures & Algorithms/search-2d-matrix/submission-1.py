class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # finding the candidate row
        lo = 0
        hi = len(matrix) - 1
        row = -1

        while lo <= hi:
            mid = (lo+hi) // 2
            if target >= matrix[mid][0] and target <= matrix[mid][len(matrix[mid])-1]:
                row = mid
                break
            
            elif target >= matrix[mid][0] and target >= matrix[mid][len(matrix[mid])-1]:
                lo = mid + 1

            else:
                hi = mid - 1

        if row == -1:
            return False

        # performing binary search on the candidate row 

        lo = 0
        hi = len(matrix[row])-1

        while lo <= hi:
            mid = (lo + hi) // 2
            if matrix[row][mid] == target:
                return True
            
            elif matrix[row][mid] < target:
                lo = mid + 1
            
            else:
                hi = mid - 1

        
        return False

        

        