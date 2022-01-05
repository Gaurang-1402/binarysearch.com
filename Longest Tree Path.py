# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# approach
# this one is quiet tricky imo
# we have to maintain both the diameter and height of the tree. How do we do this?
# many ways but the way I have gone for is by keeping the height in the return value
# and calculating and storing max diameter globaly

# maxDiameter at any point is either the maxDiameter of either children, or
# the sum of leftHeight, rightHeight and 1.

# analysis
# we go through each node once so the time complexity is
# T = O(n)

# worst case scenario we have a long linked tree where recursion stack will have n nodes
# S = O(n)

class Solution:

    def solve(self, root):
        def updateDiameterAndGetHeight(root):
            if root is None:
                # height is 0 if root is None
                return 0

            leftHeight = updateDiameterAndGetHeight(root.left)
            rightHeight = updateDiameterAndGetHeight(root.right)

            # access and update the global variable
            maxDiameterSoFar[0] = max(maxDiameterSoFar[0], leftHeight + rightHeight + 1) # maxDiameter can be addition of heights + 1 for root

            # keep returning the heights
            return max(leftHeight, rightHeight) + 1

        # edge case
        if not root:
            return 0

        # this is a trick to have a global updatable max variable
        # maintain it as len of 1 and when you return, return the 0th element each time
        maxDiameterSoFar = [0]

        updateDiameterAndGetHeight(root)

        return maxDiameterSoFar[0]
