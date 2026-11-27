class Solution:
    def rob(self, nums: list[int]) -> int:
        
        n = len(nums)
        
        if n <= 2:
            return max(nums)
        
        dp = [0] * n

        dp[0] = nums[0]
        dp[1] = max(nums[0] , nums[1])

        for i in range(2 , n):

            take = dp[i - 2] + nums[i]
            give = dp[i - 1]
            dp[i] = max(take , give)

        return dp[-1]