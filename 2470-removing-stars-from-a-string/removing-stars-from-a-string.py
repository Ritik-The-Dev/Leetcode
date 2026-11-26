class Solution:
    def removeStars(self, s: str) -> str:
        
        stack = []

        for char in s :
            if char == "*" and stack:
                stack.pop()
            else:
                stack.append(char)

        while stack and stack[-1] == "*":
            stack.pop()
        
        return "".join(stack)