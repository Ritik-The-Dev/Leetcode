class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        
        m = len(matrix)
        n = len(matrix[0])

        result = [[0] * m for _ in range(n)]

        for row in range(m):
            for col in range(n):
                result[col][row] = matrix[row][col]

        return result