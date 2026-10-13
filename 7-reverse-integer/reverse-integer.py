class Solution:
    def reverse(self, x: int) -> int:
        
        sign = 1 

        if x < 0:
            sign = -1
            x = x * -1

        reverse = 0

        while x > 0 :
            num = x % 10
            reverse = (reverse * 10) + num
            x //= 10

        result = reverse * sign

        if result < -(2 ** 31) or result > (2 ** 31 - 1):
            return 0

        return result