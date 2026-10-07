class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        
        buy = [float('inf')] * k
        profit = [0] * k

        for price in prices:
            buy[0] = min(buy[0] , price)
            profit[0] = max(profit[0] , price - buy[0])

            for i in range(1, k):
                buy[i] = min(buy[i] , price - profit[i - 1])
                profit[i] = max(profit[i] , price - buy[i])

        return profit[k - 1]