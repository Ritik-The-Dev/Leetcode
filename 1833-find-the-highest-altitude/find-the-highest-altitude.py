class Solution:
    def largestAltitude(self, gains: list[int]) -> int:
        
        curr = 0
        result = 0

        for gain in gains:
            curr += gain
            result = max(result , curr)

        return result