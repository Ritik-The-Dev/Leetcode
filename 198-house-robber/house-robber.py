class Solution:
    def rob(self, nums: list[int]) -> int:
        
        n = len(nums)
        
        result = float('-inf')
        dp = {}
        
        def recursive(curr, money):
            
            nonlocal result

            if curr >= n:
                return money

            if (curr,money) in dp:
                return dp[(curr,money)]

            amount1 = recursive(curr + 2 , money + nums[curr])
            amount2 = recursive(curr + 1 , money)
            
            dp[(curr,money)] = max(amount1 or 0 , amount2 or 0)
            result = max(result , dp[(curr,money)])
            
        recursive(0 , 0)

        return result