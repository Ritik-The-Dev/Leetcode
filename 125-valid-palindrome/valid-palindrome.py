class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        i  = 0
        j = len(s)- 1

        while i <= j:
            firstChar = s[i].isalnum()
            lastChar =  s[j].isalnum()

            if not firstChar or not lastChar:
                if not  firstChar :
                    i +=  1
                if not lastChar:
                    j -= 1
            else:
                if s[i].lower() != s[j].lower():
                    return False
                i += 1
                j -= 1

        return True