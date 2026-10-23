class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        
        m = len(mat)
        n = len(mat[0])

        # i = 0
        # j = len(n) - 1

        # row = 0

        # isEven = m % 2 == 0 

        # totalSum = 0

        # while row < m :
        #     if (isEven and (row == m / 2)):
        #         totalSum += (mat[row][i] + mat[row][i + 1])
        #     elif (isEven and row == (m / 2) + 1):

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