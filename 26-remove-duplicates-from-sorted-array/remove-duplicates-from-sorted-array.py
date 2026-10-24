class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        
        i = 0
        
        total  = 0
        pos = 0

        while i < len(nums):
            while 0 < i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
            
            if i == len(nums):
                return total

            nums[pos] = nums[i]
            pos += 1
            i += 1
            total += 1

        return total

        
        

        return curr
