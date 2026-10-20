class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freq = {}

        left = 0
        maxLen = 0

        result = float('-inf')

        for idx ,right in enumerate(s):
            freq[right] = freq.get(right , 0) + 1
            maxLen = max(maxLen , freq[right])

            while (idx - left + 1) - maxLen > k:
                freq[s[left]] -= 1
                left += 1

            result = max(result , idx - left + 1)

        return result

        
