class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        
        low = 0
        high = max(piles)

        def canEat(num):
            totalTime = 0

            for pile in piles:
                totalTime += ceil(pile / num)

            return totalTime <= h

        while low < high:
            mid = (low + high) // 2
            
            if mid > 0 and canEat(mid):
                high = mid
            else:
                low = mid + 1

        return low