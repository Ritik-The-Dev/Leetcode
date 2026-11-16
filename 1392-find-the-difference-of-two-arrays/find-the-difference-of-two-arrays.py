class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:

        nums1 = list(set(nums1))       
        nums2 = list(set(nums2))
                
        nums1.sort()
        nums2.sort()

        result = [[] , []]

        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] != nums2[j]:
                if nums1[i] < nums2[j]:
                    result[0].append(nums1[i])
                    i += 1
                else:
                    result[1].append(nums2[j])
                    j += 1
            else:
                i += 1
                j += 1
        
        while i < len(nums1):
            result[0].append(nums1[i])
            i += 1
        
        while j < len(nums2):
            result[1].append(nums2[j])
            j += 1

        return result