class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        isTarget = {}

        for idx in range(len(nums)):
            i = nums[idx]
            newTarget = target - i
            if newTarget in isTarget:
                return [isTarget[newTarget] , idx ]
            isTarget[i] = idx

        return -1