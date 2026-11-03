class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        openingBraces = ["(","{","["]
        
        validPairs = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for bracket in s :
            if bracket not in openingBraces and not stack:
                return False
            elif bracket in openingBraces:
                stack.append(bracket)
            else:
                if stack[-1] != validPairs[bracket]:
                    return False
                stack.pop()

        return not len(stack)
                