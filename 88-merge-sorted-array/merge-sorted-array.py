class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        i = 0
        j = 0
        idx = len(nums1) - len(nums2)

# [1 ,2,2,3,0,0]
# i = 3
# j = 1  

        while i < len(nums1) and j < len(nums2):
            if i == idx:
                nums1[idx] = nums2[j]
                idx += 1
                j += 1
            elif nums1[i] <= nums2[j] :
                i += 1
            else :
                nums1[i] , nums1[idx] = nums2[j] , nums1[i]
                i += 1
                j += 1
                idx += 1
        
        nums1.sort()
