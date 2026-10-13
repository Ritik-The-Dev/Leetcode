class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        
        change = [0 , 0]

        for i in bills:
            if i == 5:
                change[0] += 1
            elif i == 10 and change[0]:
                change[1] += 1
                change[0] -= 1
            elif i == 20 and change[1] and change[0]:
                change[1] -= 1
                change[0] -= 1
            elif i == 20 and change[0] >= 3:
                change[0] -= 3
            else:
                return False

        return True
