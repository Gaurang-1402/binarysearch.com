# intuition
# two arrays so two pointers but notice we need to start popping once pushes[p1] == pushes[p2] and the order
# of pop should be reverse of order of push. Therefore, pointer approach works

# implementation
# initialize two pointers and a stack
# conditionally increment p2 as long as the last elem in the stack is the same as pops[p2] because only then popping makes sense
# pushes are made regardless
# if the stack has remaining elements, we return false, and if empty return true

# analysis
# we go through each elems in pushes and pops once and since they must be of the same length, we can define len(pushes) as n
# T = O(n)

# we save space in the stack as elems are pushed worst case we have n elems
# S = O(n)


class Solution:
    def solve(self, pushes, pops):
        currStack = []
        p1 = 0
        p2 = 0
        while p1 < len(pushes) and p2 < len(pops):
            currStack.append(pushes[p1])
            while len(currStack) and p2 < len(pops) and currStack[-1] == pops[p2]:
                p2 += 1
                currStack.pop()
            p1 += 1
        return True if len(currStack) == 0 else False

