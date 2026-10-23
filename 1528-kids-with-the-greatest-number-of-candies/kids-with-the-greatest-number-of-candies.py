class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        
        highest = max(candies)
        
        result = []

        for i in candies:
            if i == highest:
                result.append(True)
            elif (i + extraCandies) >= highest:
                result.append(True)
            else:
                result.append(False)

        return result