class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        
        string1 = list(s)

        i = 0
        j = len(s) - 1
        
        while i <= j:
            if string1[i] != string1[j]:
                if string1[i] > string1[j]:
                    string1[i] = string1[j]
                else:
                    string1[j] = string1[i]
                # string1[i] = string1[j]
            i += 1
            j -= 1

        # string2 = list(s)

        # i = len(s) - 1
        # j = 0

        # while i >= j:
        #     if string2[i] != string2[j]:
        #         string2[i] = string2[j]
        #     i -= 1
        #     j += 1

        return  "".join(string1)
        s2 = "".join(string2)

        return s1 if s1 < s2 else s2
            