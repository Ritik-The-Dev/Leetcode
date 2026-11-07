class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowels = {"a":1,"e":2,"i":3,"o":4,"u":5}
        
        n = len(s) # 9

        # i = 0      # 0
        # j = k - 1  # 2

        # count = 0  # 1

        # for i in range(k):
        #     if s[i] in vowels:
        #         count += 1

        # result = count # 3
        # # i = 3 , count = 3

        # while j < n: # 5 < 9    

        #     if s[i] in vowels:
        #         count -= 1
            
        #     i += 1
        #     j += 1

        #     if j < n and s[j] in vowels:
        #         count += 1
            
        #     result = max(result , count)

        # return result

        count = 0

        for i in range(k):
            if s[i] in vowels:
                count += 1

        result = count
    
        for idx in range(k,n):
            if s[idx - k] in vowels :
                count -= 1
            if s[idx] in vowels :
                count += 1

            result = max(result , count)

        return result