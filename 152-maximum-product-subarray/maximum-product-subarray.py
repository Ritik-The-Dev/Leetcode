class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        
        posProduct = 1 
        negProduct = 1 

        result = float('-inf') 

        for num in nums:
            
            tempPos = posProduct
            posProduct = max(num , posProduct * num , negProduct * num) # 3
            negProduct = min(num , negProduct * num , tempPos * num) # -240

            result = max(result , posProduct) #20

        return result