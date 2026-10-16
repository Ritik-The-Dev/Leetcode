class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        # for i in range(1 , len(nums),2):
        #     if nums[i] != nums[i - 1]:
        #         return nums[i - 1]

        # return nums[-1]
    
        # low = 0
        # high = len(nums) - 1

        # while low < high:
        #     mid = (low + high) // 2

        #     if mid % 2 == 1:
        #         mid -= 1
            
        #     if nums[mid] == nums[mid + 1]:
        #         low = mid + 2
        #     else:
        #         high = mid

        # return nums[high]

        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            if mid % 2 == 1:
                mid -= 1

            if nums[mid] == nums[mid + 1]:
                low = mid + 2
            else:
                high = mid

        return nums[high] or nums[low]
        
                
