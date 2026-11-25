class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        
        dp = {}

        def recursive(n):
            
            if n <= 1:
                return 0
            
            if n in dp:
                return dp[n]

            dp[n] = min(recursive(n - 1) + cost[n - 1] , recursive(n - 2) + cost[n - 2])
            return dp[n]

        return recursive(len(cost))