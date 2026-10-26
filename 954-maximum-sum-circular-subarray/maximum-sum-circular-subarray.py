class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        
        # find the biggest no and smallest no

        # 2 chize calculate kar maximum subarray sum and min subararay sum 

        #  find the max postive and min negative
        
        #   either return maximum or sum(nums) - minimum = maximum ? 
        
        maximum = max(nums)
        minimum = min(nums)

        positiveCurr = 0
        negativeCurr = 0

        for num in nums:
            tempPos = positiveCurr + num
            tempNeg = negativeCurr + num

            if tempPos < 0:
                positiveCurr = 0
            else:
                positiveCurr = tempPos
                maximum = max(maximum , tempPos)

            if tempNeg > 0:
                negativeCurr = 0
            else:
                negativeCurr = tempNeg
                minimum = min(minimum , tempNeg)
        
        if maximum < 0:
            return maximum

        return max(maximum , sum(nums) - minimum)