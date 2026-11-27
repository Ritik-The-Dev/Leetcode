class Solution:
    def rob(self, nums: list[int]) -> int:
        
        n = len(nums)
        dp = {}
        
        def recursive(curr):
            
            if curr >= n:
                return 0

            if curr in dp:
                return dp[curr]

            amount1 = nums[curr] + recursive(curr + 2)
            amount2 = recursive(curr + 1)

            dp[curr] = max(amount1 , amount2)            
            return dp[curr]
            
        return recursive(0)
