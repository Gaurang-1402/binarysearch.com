class Solution:
    def solve(self, s):

        stack = []

        closeToOpen = {")":"("}

        removalCount = 0

        for bracket in s:
            if bracket in closeToOpen.values():
                # open paren
                stack.append(bracket)
            else:
                # close paren
                if len(stack) == 0:
                    removalCount += 1
                else:
                    topParen = stack.pop()
                    if topParen == closeToOpen[bracket]:
                        continue


        return removalCount + len(stack)

