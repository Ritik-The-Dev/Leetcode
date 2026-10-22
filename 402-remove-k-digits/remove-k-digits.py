class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        arr = []

        for i in num:
            while arr and arr[-1] > i and k > 0:
                arr.pop()
                k -= 1
            
            arr.append(i)
        
        if k > 0:
            arr = arr[:-k]

        result = "".join(arr).lstrip("0")
        return result if result else "0"