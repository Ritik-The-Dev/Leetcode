class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = {}

        def recursive(i , j):
            
            if (i , j) in dp:
                return dp[(i , j)]

            if i ==  m - 1 and j == n - 1:
                return 1

            if i >= m or j >= n:
                return 0

            right = recursive(i , j + 1 )
            down  = recursive(i + 1 , j )

            dp[(i , j)] =  right + down
            return dp[(i ,  j)]

        return recursive(0 , 0)