class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        
        prev = 0
        largest = float('-inf')

        for num in nums:
            prev = max(num , prev + num)
            largest = max(largest , prev )
        
        return largest