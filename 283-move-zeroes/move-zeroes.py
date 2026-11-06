class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        
        n = len(nums)

        i = 0
        while i < n and nums[i] != 0 :
            i += 1
        
        j = i
        while j < n and nums[j] == 0:
            j += 1
        
        while i < j < n :
            nums[i],nums[j] = nums[j],nums[i]
            
            i += 1
            while i < n and nums[i] != 0 :
                i += 1
            
            j = i
            while j < n and nums[j] == 0:
                j += 1
