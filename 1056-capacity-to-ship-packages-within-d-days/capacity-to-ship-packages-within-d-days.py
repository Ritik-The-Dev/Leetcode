class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        
        low = max(weights)
        high = sum(weights)

        def canShip(maxAllowed):
            total = 1
            curr = 0
            for i in weights:
                if i + curr > maxAllowed:
                    total += 1
                    curr = 0
                
                curr += i
            
            return total <= days

        result = float('inf')

        while low <= high:
            mid = (low + high) // 2

            if canShip(mid) :
                result = min(result , mid)
                high = mid - 1
            else:
                low = mid + 1

        return result