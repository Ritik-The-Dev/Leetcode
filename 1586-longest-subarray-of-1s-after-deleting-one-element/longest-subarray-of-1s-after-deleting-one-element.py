class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        
        zero_count = 0
        result = 0

        start = 0

        for i in range(len(nums)):
            zero_count += (nums[i] == 0)

            while(zero_count > 1):
                zero_count -= (nums[start] == 0)
                start += 1

            result = max(result , i - start)

        return result