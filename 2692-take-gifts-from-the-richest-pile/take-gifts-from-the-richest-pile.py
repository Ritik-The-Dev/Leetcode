class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        import heapq

        heap = []

        for gift in gifts:
            heapq.heappush(heap , -gift)
        
        while k > 0:            
            val = -heapq.heappop(heap)
            heapq.heappush(heap , -floor(sqrt(val)))
            k -= 1

        return -sum(heap)