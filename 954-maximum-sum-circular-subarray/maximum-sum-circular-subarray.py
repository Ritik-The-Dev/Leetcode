class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        
        minimum = min(nums)
        maximum = max(nums)

        minSum  = 0
        maxSum = 0

        for num in nums:

            minTemp = minSum + num
            maxTemp = maxSum + num

            if maxTemp < 0 :
                maxSum = 0
            else:
                maxSum = maxTemp
                maximum = max(maximum , maxTemp)

            if minTemp > 0:
                minSum = 0
            else:
                minSum = minTemp
                minimum = min(minimum , minSum)

        if maximum < 0:
            return maximum

        return max(maximum , sum(nums) - minimum)