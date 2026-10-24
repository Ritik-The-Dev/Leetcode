class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        firstZero = 0

        while firstZero < len(nums) and  nums[firstZero] !=  0:
            firstZero += 1

        numAfterZero = firstZero + 1

        while numAfterZero < len(nums) and  nums[numAfterZero] == 0:
            numAfterZero += 1

        while numAfterZero < len(nums):

            nums[firstZero]  ,nums[numAfterZero]  =  nums[numAfterZero] , nums[firstZero]
            
            firstZero += 1

            while firstZero < len(nums) and  nums[firstZero] !=  0:
                firstZero += 1

            numAfterZero = firstZero + 1

            while numAfterZero < len(nums) and  nums[numAfterZero] == 0:
                numAfterZero += 1

        if  numAfterZero < len(nums) and nums[numAfterZero] != 0:
            nums[firstZero] ,nums[numAfterZero] =  nums[numAfterZero] , nums[firstZero] 

        return nums