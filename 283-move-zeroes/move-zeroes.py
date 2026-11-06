class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        
        count = nums.count(0)

        nums[:] = [x for x in nums if x != 0]
        nums += [0] * count
        