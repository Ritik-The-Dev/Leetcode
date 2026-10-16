class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowelsIndex = []
        
        s = list(s)

        vowels = ["a","e","i","o","u"]

        for idx,num  in enumerate(s):
            if num.lower() in vowels:
                vowelsIndex.append(idx)

        i = 0
        j = len(vowelsIndex) - 1

        while i < j:
            s[vowelsIndex[i]],s[vowelsIndex[j]] = s[vowelsIndex[j]],s[vowelsIndex[i]]
            i += 1
            j -= 1
            
        return "".join(s)
            