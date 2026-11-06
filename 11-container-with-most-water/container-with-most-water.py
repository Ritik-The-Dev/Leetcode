class Solution:
    def maxArea(self, height: list[int]) -> int:
        
        n = len(height)

        i = 0
        j = n - 1

        largest = float('-inf')

        while i < j :
            val1 = height[i]
            val2 = height[j]
            
            largest = max(largest , (min(val1 , val2) * (j - i)))

            if val1 > val2:
                j -= 1
            else:
                i += 1

        return largest