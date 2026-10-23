class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        
        m = len(mat)
        n = len(mat[0])

        start_col = 0
        end_col = n - 1

        start_row = 0
        end_row = m - 1

        total = 0

        while start_row < end_row:
            total += (mat[start_row][start_col] + mat[start_row][end_col] + mat[end_row][start_col] + mat[end_row][end_col])
            start_row += 1
            end_row -= 1
            start_col += 1
            end_col -= 1

        if m % 2 != 0:
            total += (mat[start_row][start_col])

        return total