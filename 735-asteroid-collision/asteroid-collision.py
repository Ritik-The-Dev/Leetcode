class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        n = len(asteroids)
        skippedElem = []
        i = n - 1
  
        while i > 0:
            lastValue = asteroids[i]
            secondLastValue = asteroids[i - 1]

            if lastValue < 0 and secondLastValue >= 0 :
                if abs(lastValue) > abs(secondLastValue):
                    asteroids[i - 1] = lastValue
                elif abs(lastValue) < abs(secondLastValue):
                    asteroids[i - 1] = secondLastValue
                else :
                    asteroids.pop()
                    i -= 1
                if len(skippedElem) and skippedElem[-1] < 0 :
                    asteroids[i] = skippedElem[-1]
                    skippedElem.pop()
                else:
                    asteroids.pop()
                    i -= 1 
            else:
                skippedElem.append(asteroids[i])
                asteroids.pop()
                i -= 1      

        for j in range(len(skippedElem) -1 , -1, -1):
            asteroids.append(skippedElem[j])

        return asteroids              
                                    
