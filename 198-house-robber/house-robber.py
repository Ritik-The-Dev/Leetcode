class Solution:
    def rob(self, nums: list[int]) -> int:
        
        n = len(nums)
        dp = {}
        
        def recursive(curr):

            if curr in dp:
                return dp[curr]

            if curr >= n:
                return 0

            robed = nums[curr] + recursive(curr + 2)
            notRobed = recursive(curr + 1)
            
            dp[curr] = max(robed , notRobed)
            return dp[curr]
            
        return recursive(0)