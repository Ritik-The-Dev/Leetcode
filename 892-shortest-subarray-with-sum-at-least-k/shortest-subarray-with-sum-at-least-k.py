class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        
        import heapq

        if k in nums:
            return 1

        smallTrack = []

        prefix = [0] #[54 , 49 , 102 , 83 , 168]
        
        result = float('inf')

        for j in range(len(nums)):
            curr = nums[j] + prefix[j] # 3
            prefix.append(curr) # [ 0, 2 , 1 , 3]
            heapq.heappush(smallTrack , (curr , j + 1)) #[(1 , 2)]

            if curr >= k:
                result = min(result , j + 1)

            while curr - smallTrack[0][0] >= k :
                result = min(result , j -  smallTrack[0][1]  + 1)
                heapq.heappop(smallTrack)
                
        return -1 if result == float('inf') else result

