class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        
        change = {
            5 : 0,
            10 : 0
        }

        for i in bills:
            if i == 10 and change[5]:
                change[10] += 1
                change[5] -= 1
            elif i == 20 and ((change[10] and change[5]) or change[5] >= 3):
                if change[10]:
                    change[10] -= 1
                    change[5] -= 1
                else:
                    change[5] -= 3
            elif i == 5:
                change[5] += 1
            else:
                return False

        return True
