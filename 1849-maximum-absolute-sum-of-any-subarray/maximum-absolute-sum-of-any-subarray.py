class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        
        currMax = currMin = 0
        maximum = minimum = 0

        for num in nums:

            currMax = max(num , currMax + num)
            currMin = min(num , currMin + num)

            maximum = max(maximum, currMax) 
            minimum = min(minimum, currMin)

        return max(maximum , abs(minimum)) 