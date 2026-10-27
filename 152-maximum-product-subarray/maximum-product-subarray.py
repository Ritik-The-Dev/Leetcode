class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        
        pos = 1
        neg = 1

        result = float('-inf')

        for num in nums:
            pos , neg = max( num , pos * num, neg * num) , min (num , pos * num , neg * num)
            result = max(result , pos , neg)

        return result