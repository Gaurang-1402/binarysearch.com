# approach
# Since we need to get access to the previous element to check for a duplicate, we need to use a stack.
# We can only allow an element to enter the stack if the element at the top of the stack is not a duplicate.
# As we traverse through the string and append to the stack, If we find that the current element is a duplicate,
# we pop the duplicate off the stack and keep traversing the string until all duplicates have been avoided
# Finally we convert the stack into a string and return it.

# analysis
# Time Complexity
# T = O(n) although we have a nested while loop, we will never traverse more than n elements where n is len(s)

# Space Complexity
# S = O(n) because we use a stack to store n elements where n is len(s)

class Solution:
    def solve(self, s):
        stack = []
        i = 0
        while i < len(s):
            if i == 0:
                stack.append(s[i])
                i += 1
                continue

            if len(stack) and s[i] == stack[-1]:
                duplicateElem = stack.pop()
                while i < len(s) and s[i] == duplicateElem:
                    i += 1
            else:
                stack.append(s[i])
                i += 1
        return "".join(stack)
