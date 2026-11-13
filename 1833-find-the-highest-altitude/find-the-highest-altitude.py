class Solution:
    def largestAltitude(self, gain: list[int]) -> int:

        highest = 0
        currentPrefix = 0

        for i in range(len(gain)):
            currentPrefix += gain[i]
            if currentPrefix > highest:
                highest = currentPrefix 
        
        return highest