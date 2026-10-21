class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                curr = matrix[i][j]
                if curr == target:
                    return True
                elif curr < target:
                    continue
                else:
                    break
        
        return False