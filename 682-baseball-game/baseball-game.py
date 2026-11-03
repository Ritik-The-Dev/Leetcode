class Solution:
    def calPoints(self, operations: list[str]) -> int:
        
        stack = []

        for operation in operations:
            n = len(stack)

            if operation == "+":
                stack.append(stack[n - 1] + stack[n - 2])
            elif operation == "D":
                stack.append(stack[-1] * 2)
            elif operation == "C":
                stack.pop()
            else:
                stack.append(int(operation))

        return sum(stack)