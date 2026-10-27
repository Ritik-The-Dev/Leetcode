class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        
        maximum = max(nums)
        minimum = min(nums)

        currMax = 0
        currMin = 0

        for num in nums:
            currMax = max(currMax , 0) + num
            currMin = min(currMin , 0) + num

            maximum = max(currMax , maximum)
            minimum = min(currMin , minimum)

        if maximum < 0:
            return maximum

        return max(maximum , sum(nums) - minimum)