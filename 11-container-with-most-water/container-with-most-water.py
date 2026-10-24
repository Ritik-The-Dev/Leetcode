class Solution:
    def maxArea(self, height: list[int]) -> int:
        
        result = float('-inf')

        i = 0
        j = len(height) - 1

        while i  <  j:
            currentCapacity = min(height[i] , height[j]) * (j - i)
            result = max(currentCapacity , result)
            
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return result