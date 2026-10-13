class Solution:
    def reverseWords(self, s: str) -> str:
        
        split = s.split(" ")
        reverse = ""

        for i in split:
            if i :
                reverse = i + " " + reverse 

        return reverse[:-1]