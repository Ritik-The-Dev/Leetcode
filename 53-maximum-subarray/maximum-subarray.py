class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        largestSum = max(nums)

        currSum = 0

        for i in nums : 
            temp = currSum + i
            if temp < 0:
                currSum = 0
            else:
                currSum = temp
                largestSum = max(largestSum , temp)

        return largestSum     