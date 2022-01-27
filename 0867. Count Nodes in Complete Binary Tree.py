# approach
# check this video out: https://www.youtube.com/watch?v=CvrPf1-flAA

# we have to check if we have
# how to do this?
# go to the leftmost node and check the height
# go to the rightmost node and check the height
# if both heights match, we have a proper binary tree --> Use this formula
# formula to count nodes using levels --> 2**(levels) - 1

# otherwise check for proper binary trees in left and right nodes

# analysis
# time and space are slightly complicated to analyze, check the video out https://www.youtube.com/watch?v=CvrPf1-flAA
# T = O((log(n))**2)
# S = O((log(n))**2)

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):

        def completeTreeCounter(root):

            # formula to count nodes using levels --> 2**(levels) - 1

            if root is None:
                return 0

            # find the leftmost height

            leftNode = root.left
            leftHeight = 1

            while leftNode is not None:
                leftNode = leftNode.left
                leftHeight += 1

            # find the leftmost height
            rightNode = root.right
            rightHeight = 1

            while rightNode is not None:
                rightNode = rightNode.right
                rightHeight += 1

            if leftHeight == rightHeight:
                return 2**leftHeight - 1

            # put a +1 to account for current node
            return 1 + completeTreeCounter(root.left) + completeTreeCounter(root.right)

        return completeTreeCounter(root)
