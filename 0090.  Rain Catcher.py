# approach
# watch this: https://www.youtube.com/watch?v=ZI2z5pq0TqA

# the idea is simple for any given index i, we need to get the minimum height between the
# maximum possible heights on the left and right of i

# amount of water trapped = min(leftMaxHeight, rightMaxHeight) - heightAtI

# how to do this?
# we make a leftMax arr that starts traversal from the left
# where we add the maxHeightSeenSoFar from index i from index 0

# we make a rightMax arr that starts traversal from the right
# where we add the maxHeightSeenSoFar from index i from index len(nums)-1
# (this will require us to do couple of reversals be careful about this)

# finally, we finally take the min of leftMax and rightMax and use the formula
# amount of water trapped = min(leftMaxHeight, rightMaxHeight) - heightAtI

# analysis
# we at most traverse through the array of n items 3 times so time complexity is
# T = O(n)

# we store 2n elements in arrs so space complexity is
# S = O(n)
# ^^this can be improved watch the video

class Solution:
    def solve(self, nums):
        if len(nums) <= 2:
            return 0

        leftMax = [nums[0]]
        for i in range(1, len(nums)):
            leftMax.append(max(leftMax[i - 1], nums[i]))

        rightMax = [nums[len(nums) - 1]]
        nums.reverse() # reverse nums so that the reverse traversal to make right is possible
        for i in range(1, len(nums)):
            rightMax.append(max(rightMax[i - 1], nums[i]))

        nums.reverse() # reverse nums to get them in the original form
        rightMax.reverse() # reverse right so that the order of rightMax is correct

        totalRainCollected = 0

        for i in range(len(nums)):
            if (min(leftMax[i], rightMax[i]) - nums[i]) > 0:
                totalRainCollected += min(leftMax[i], rightMax[i]) - nums[i]

        return totalRainCollected

