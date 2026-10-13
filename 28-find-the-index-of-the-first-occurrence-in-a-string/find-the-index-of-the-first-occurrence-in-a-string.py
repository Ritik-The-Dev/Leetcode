class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if len(haystack) <= len(needle):
            if haystack == needle:
                return 0
            else:
                return -1

        targetlength = len(needle)

        for i in range(len(haystack)):
            curr = haystack[i]
            if curr == needle[0]:
                if (i + targetlength) <= len(haystack) and haystack[i : i + targetlength] == needle:
                    return i

        return -1
