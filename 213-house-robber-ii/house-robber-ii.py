class Solution:
    def rob(self, nums: list[int]) -> int:
        
        n = len(nums)
        
        if n <= 2:
            return max(nums)

        def recursive(dp , curr, end):

            if curr >= end:
                return 0

            if curr in dp:
                return dp[curr]

            rob = nums[curr] + recursive(dp , curr + 2 , end)
            notRob = recursive(dp , curr + 1, end)
            
            dp[curr] = max(rob,notRob)
            return dp[curr]

        return max(recursive({} , 0 , n - 1) , recursive({} , 1 , n))