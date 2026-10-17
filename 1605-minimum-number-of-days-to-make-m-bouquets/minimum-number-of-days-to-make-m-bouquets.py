class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        if len(bloomDay) < m * k :
            return -1
        
        def checkBloom(days):
            total = 0
            i = 0
            
            for bloom in bloomDay:
                if bloom <= days:
                    i += 1

                    if i == k:
                        total += 1
                        i = 0
                else:
                    i = 0

            return total

        low = min(bloomDay)
        high = max(bloomDay)

        while low < high :

            mid = (low + high) // 2

            if checkBloom(mid) >= m:
                high = mid
            else:
                low = mid + 1
            
        return low