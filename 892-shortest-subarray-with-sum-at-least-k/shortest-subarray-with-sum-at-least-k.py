class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        
        import heapq

        prefix_sum = 0
        
        minheap = [(0 ,0)]
        
        result = float('inf')

        for idx , num in enumerate(nums):
            prefix_sum += num

            while minheap and  prefix_sum - minheap[0][0] >= k:
                prev_sum , prev_idx = heapq.heappop(minheap)
                result = min(result , idx - prev_idx + 1)
            
            heapq.heappush(minheap , (prefix_sum , idx + 1))
            
        # if k in nums:
        #     return 1 #O(n)

        # smallTrack = [] #minHeap

        # prefix = [0]
        
        # result = float('inf')

        # for j in range(len(nums)):
        #     curr = nums[j] + prefix[j] # 3
        #     prefix.append(curr) # [ 0, 2 , 1 , 3]
        #     heapq.heappush(smallTrack , (curr , j + 1)) #[(1 , 2)] ( log n )

        #     if curr >= k:
        #         result = min(result , j + 1)

        #     while curr - smallTrack[0][0] >= k : #O(n)
        #         result = min(result , j -  smallTrack[0][1]  + 1)
        #         heapq.heappop(smallTrack)
                
        # #Tc - Worst = n^2 else n log n
        # #Sc - O(n)

        return -1 if result == float('inf') else result

