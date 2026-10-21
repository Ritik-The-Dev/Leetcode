class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])

        low = 0
        high = n - 1

        while low < m and high > -1:
            
            curr = matrix[low][high]

            if curr == target:
                return True
            elif curr < target:
                low += 1
            else:
                high -= 1

        return False