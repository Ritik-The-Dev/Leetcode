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
            i += 1
            j -= 1
            
        return  "".join(string1)