class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        
        posProduct = 1
        negProduct = 1

        result = float('-inf')

        for num in nums:
            posProduct , negProduct = max(num , posProduct * num , negProduct * num) ,  min(num , posProduct * num , negProduct * num)

            result = max(posProduct , result , negProduct)

        return result