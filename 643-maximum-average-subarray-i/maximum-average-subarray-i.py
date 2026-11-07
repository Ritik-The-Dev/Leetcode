class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        
        n = len(nums)

        if k <= 1:
            return max(nums)

        prefix = [0]
        for i in range(n):
            prefix.append(prefix[i] + nums[i])

        # prefix = [0 , 0 , 1 , 2, 5, 8] 
        i = 0
        j = k

        result = float('-inf')

        while j <= n :
            curr = prefix[j] - prefix[i]
            result = max(result , curr / k )
            i += 1
            j += 1
        
        return result