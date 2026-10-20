class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        
        curr = 0 # 5

        result = float('-inf') # 6

        for i in nums:
            curr = max(i + curr , i) # 5 , 4
            result = max(result , curr)

        return result