class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        min_price = prices[0]
        profit = 0

        for price in prices:
            currProfit = price - min_price
            min_price = min(min_price , price)
            profit = max(profit , currProfit)
        
        return profit