class Solution:
    def isPalindrome(self, x: int) -> bool:

        org = x
        reverse = 0
        
        while x > 0:
            num = x % 10
            reverse = reverse * 10 + num
            x  = x // 10

        return reverse == org 
        
