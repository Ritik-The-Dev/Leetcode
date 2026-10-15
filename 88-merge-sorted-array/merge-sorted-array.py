class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # j = len(nums2)

        # while j :
        #     nums1.pop()
        #     j -= 1

        # nums1.extend(nums2)
        # nums1.sort()

        
        i = m - 1
        j = n - 1
        idx = m + n - 1 
# [4,5,3, 0,0,6]

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[idx] = nums1[i]
                i -= 1
            else:
                nums1[idx] = nums2[j]
                j -= 1
            idx -= 1
        
        while j >= 0:
            nums1[idx] = nums2[j]
            j -= 1
            idx -= 1
