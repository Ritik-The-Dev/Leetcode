class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        
        low = max(weights)
        high = sum(weights)

        result = float('inf')

        def canShip(weight):
            curr = 0    
            currDays = 1

            for num in weights:
                if curr + num > weight:
                    currDays += 1
                    curr = num
                else:
                    curr += num

            return currDays <= days

        while low <= high:

            mid = (low + high) // 2

            if canShip(mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1

        return result