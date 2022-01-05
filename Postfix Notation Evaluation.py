
class Solution:
    def solve(self, exp):

        stack = []

        for char in exp:
            if char not in "+-*/":
                stack.append(int(char))
            else:
                arg1 = stack.pop()
                arg2 = stack.pop()

                if char == "+":
                    stack.append(arg1 + arg2)
                elif char == "-":
                    stack.append(arg2 - arg1)
                elif char == "*":
                    stack.append(arg1 * arg2)
                elif char == "/":
                    stack.append(int(arg2 / arg1))

        return stack.pop()
