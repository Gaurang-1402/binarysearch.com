# approach
# the core idea is for any given root, maintain the minimum val and max val in children
# and then compare measure the largest diff between
# i) rootVal - min
# ii) max - rootVal

# we cannot take max - min into consideration because then we would be taking cases where max and min are
# not from the same path root to leaf

# we can only find the max diff between two nodes IF THEY ARE ON THE SAME PATH FROM root to leaf

# analysis
# we go through each node so total time taken is
# T = O(n)

# in case of skewed tree, we occupy n stackframes so space complexity is
# S = O(n)

class Solution:
    def solve(self, root):

        largestDiff = [float("-inf")]

        def getLargestDiff(root):
            if root is None:
                return (None, None)

            currMax = root.val
            currMin = root.val

            leftMax, leftMin = getLargestDiff(root.left)

            if leftMax is not None:
                currMax = max(currMax, leftMax)

            if leftMin is not None:
                currMin = min(currMin, leftMin)

            rightMax, rightMin = getLargestDiff(root.right)

            if rightMax is not None:
                currMax = max(currMax, rightMax)

            if rightMin is not None:
                currMin = min(currMin, rightMin)

            largestDiff[0] = max(largestDiff[0], abs(root.val - currMin), abs(currMax - root.val))

            return (currMax, currMin)

        getLargestDiff(root)

        return 0 if largestDiff[0] == float("-inf") else largestDiff[0]
