class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        
        low = 1
        high = max(piles)

        result = float('inf')

        def canEat(speed):

            curr = 0

            for pile in piles:
                curr += ceil(pile / speed)

                if curr > h:
                    return False
            
            return curr <= h

        while low <= high :

            mid = (low + high) // 2

            if canEat(mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1

        return result
