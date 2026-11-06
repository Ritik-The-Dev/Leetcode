class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        i = 0
        j = len(nums) - 1

        pairs = 0

        while i < j:
            
            total = nums[i] + nums[j]

            if total == k :
                i += 1
                j -= 1
                pairs += 1
            elif total > k:
                j -= 1
            else:
                i += 1

        return pairs