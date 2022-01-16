# approach
# watch this: https://www.youtube.com/watch?v=dJ7sWiOoK7g&t=624s
# this is essentially a combination of the greedy method and sliding window
# the window starts from en elem (left) and ends at furthestJumpInWindow(right) and the furthestJumpInWindow choice is the greedy method

# we keep shifting the window until right reaches the second last elem in the list
# because we don't need to cross the last elem in the list

# analysis
# in the worst case scenario, entire array has 1s so we go through each elem then time taken
# is
# T = O(n)

# we don't use any extra space so space complexity is
# S = O(k)

class Solution:
    def solve(self, nums):

        left = 0
        right = 0

        jumps = 0

        while right < len(nums) - 1:
            furthestJumpInWindow = 0

            for i in range(left, right + 1):
                jump = nums[i]
                furthestJumpInWindow = max(furthestJumpInWindow, i + jump)

            # left is updated to the elem directly after right
            left = right + 1


            # right becomes the elem that is furthest in the jump
            right = furthestJumpInWindow

            # each time window is shifted, a jump is made
            jumps += 1

        return jumps
