class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        
        maximum = max(nums)
        minimum = min(nums)

        currMax = 0
        currMin = 0

        for num in nums:
            tempMax = currMax + num
            tempMin = currMin + num

            if tempMax < 0:
                currMax = 0
            else:
                currMax = tempMax
                maximum = max(maximum , tempMax)

            if tempMin > 0:
                currMin = 0
            else:
                currMin = tempMin
                minimum = min(minimum , tempMin)

        
        if maximum < 0:
            return maximum

        return max(maximum , sum(nums) - minimum)