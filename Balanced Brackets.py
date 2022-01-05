class Solution:
    def solve(self, s):

        stack = []

        for char in s:
            if char == "(":
                stack.append(char)
            else:
                if stack:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0


        
