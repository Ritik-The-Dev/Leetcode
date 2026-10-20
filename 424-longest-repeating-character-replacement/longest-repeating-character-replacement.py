class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freq = {}

        left = 0
        maxLen = 0

        result = float('-inf')

        for right ,char in enumerate(s):
            freq[char] = freq.get(char , 0) + 1
            maxLen = max(maxLen , freq[char])

            while (right - left + 1) - maxLen > k:
                freq[s[left]] -= 1
                left += 1

            result = max(result , right - left + 1)

        return result

        
