class Solution:
    def rob(self, nums: list[int]) -> int:
        
        # n = len(nums)
        
        # if n <= 2:
        #     return max(nums)

        # def recursive(dp , curr, end):

        #     if curr > end:
        #         return 0

        #     if curr in dp:
        #         return dp[curr]

        #     rob = nums[curr] + recursive(dp , curr + 2 , end)
        #     notRob = recursive(dp , curr + 1, end)
            
        #     dp[curr] = max(rob,notRob)
        #     return dp[curr]

        # return max(recursive({} , 0 , n - 2) , recursive({} , 1 , n - 1))


        # tabulation

        n = len(nums)

        if n <= 2:
            return max(nums)
            
        dp = [0] * (n - 1)

        dp[0] = nums[0]
        dp[1] = max(nums[0] , nums[1])

        for i in range(2 , n - 1):
            take = nums[i] + dp[i - 2]
            give = dp[i - 1]
            dp[i] = max(give, take)

        robFirst = dp[-1]
        dp = [0] * n

        dp[1] = nums[1]
        dp[2] = max(nums[1] , nums[2])

        for i in range(3 , n):
            take = nums[i] + dp[i - 2]
            give = dp[i - 1]
            dp[i] = max(give, take)
        
        return max(robFirst , dp[-1])