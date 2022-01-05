class Solution:
    def solve(self, s):

        stack = []


        i = 0

        while i < len(s):
            if (i + 1 < len(s) and s[i] == "<" and s[i + 1] == "-"):

                if len(stack) != 0:
                    stack.pop()
                i += 2

            else:
                stack.append(s[i])
                i += 1

        return "".join(stack)

        
