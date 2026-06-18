class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            lo = 0
            hi = len(matrix[0])-1
            while lo <=hi:
                mid = (lo+hi) // 2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return False

        