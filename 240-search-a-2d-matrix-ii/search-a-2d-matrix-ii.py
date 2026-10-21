class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])
        
        # row = []
        # col = []

        for i in range(m):
            for j in range(n):
                curr = matrix[i][j]
                if matrix[i][j] == target:
                    return True
                elif matrix[i][j] < target:
                    continue
                else:
                    break
        
        return False