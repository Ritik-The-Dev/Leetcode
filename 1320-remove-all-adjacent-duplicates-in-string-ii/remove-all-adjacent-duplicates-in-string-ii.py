class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        curr = []
        
        for i in s:
            if curr and curr[-1][0] == i:
                curr[-1][1] += 1
            else:
                curr.append([i , 1])
            
            if curr[-1][1] == k:
                curr.pop()

        result = ""
        
        for val , count in curr:
            for i in range(count):
                result += val

        return result