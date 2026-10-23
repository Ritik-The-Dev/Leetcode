class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        
        m = len(matrix)
        n = len(matrix[0])

        newMatrix = [[0] * m  for _ in range(n)]

        for row in range(n): #0
            for col in range(m): #2
                newMatrix[row][col] = matrix[col][row]
                # newMatrix[col][row] = matrix[row][col]

        return newMatrix

        # m = 2 
        # n = 3 
        # [1 , 4]
        # [2 , 0]
        # [0 , 0]

