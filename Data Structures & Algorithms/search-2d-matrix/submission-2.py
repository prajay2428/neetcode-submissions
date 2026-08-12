class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first findout in which row the target could exist
        # and then choose the row and perform binary search

        rows, columns = len(matrix), len(matrix[0])

        top = rows -1
        bottom = 0

        while bottom <= top:
            mid = (top + bottom) // 2

            if target < matrix[mid][0]:
                top = mid - 1
            
            elif target > matrix[mid][columns-1]:
                bottom = mid + 1
            
            else:
                left = 0
                right = columns - 1
                while left <= right:
                    m =( left + right) // 2

                    if target == matrix[mid][m]:
                        return True
                    elif target < matrix[mid][m]:
                        right = m - 1
                    
                    else:
                        left = m + 1
                return False
        return False
                

