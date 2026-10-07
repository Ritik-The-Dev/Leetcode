class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        dp = {}

        def recursive(i , j):

            if (i , j) in dp:
                return dp[(i , j)]

            if  i >= len(text1) or j >= len(text2):
                return 0

            if text1[i] == text2[j]:
                return 1 + recursive(i +1 , j +1 )
            
            res1 = recursive(i + 1 , j )
            res2 = recursive(i , j + 1 )

            dp[(i , j)] = max(res1 , res2)
            return dp[(i , j)]

        return recursive(0, 0 )