class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        
        n = len(nums)
        result = []

        def recursive(i , curr):
            if i >= n:
                result.append(curr[:])
                return 

            for idx in range(i , n):

                curr[idx] , curr[i] = curr[i] , curr[idx]
                recursive(i + 1, curr)
                curr[idx] , curr[i] = curr[i] , curr[idx]

        recursive(0 , nums)
        return result