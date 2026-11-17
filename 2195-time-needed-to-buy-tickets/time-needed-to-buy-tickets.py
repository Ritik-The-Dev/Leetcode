class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        
        from collections import deque

        queue = deque(tickets)
        count = 0

        while queue:
            count += 1
            val = queue.popleft()
            val -= 1

            if val > 0:
                queue.append(val)
            
            if k == 0 and val == 0:
                return count
            
            k -= 1

            if k < 0:
                k = len(queue) - 1

        return count