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

        dp1 = [0] * n
        dp2 = [0] * n


        dp1[0] , dp1[1] = nums[0] , max(nums[0] , nums[1])
        dp2[1] , dp2[2] = nums[1] , max(nums[1] , nums[2])

        for i in range(2 , n):
            
            if i != 2:
                take = nums[i] + dp2[i - 2]
                give = dp2[i - 1]
                dp2[i] = max(give, take)
            
            if i != n - 1:
                take = nums[i] + dp1[i - 2]
                give = dp1[i - 1]
                dp1[i] = max(give, take)
                
        return max(dp1[n - 2] , dp2[-1])