class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        
        n = len(nums)

        result = []

        def recursive(i , curr):

            if i >= n:
                result.append(curr[:])
                return 

            for idx in range(i , n):

                curr[i] , curr[idx] = curr[idx] , curr[i]
                recursive(i + 1 , curr)
                curr[i] , curr[idx] = curr[idx] , curr[i]

        recursive(0 , nums)
        return result