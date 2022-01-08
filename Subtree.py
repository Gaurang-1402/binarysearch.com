# approach
# We only explore target if we find that the val at target matches the val at root

# For base cases, we always return False if either target or root are None because it would be impossible for target to be a subtree of root then.
# If we find that val at target matches val at root, we get strict about the bools returned by the children. If the vals at roots do not match, we
# are liberal in checking if vals at either of the children of root match target

# Time Complexity
# O(n) we go through each node in the larger tree once and at worst go through 2n nodes with n iterations

# Space Complexity
# O(n) the max number of stackframes occupied at any point will be n in case we have a skewed tree

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, target):

        def checkSubTree(root, target):
            if root is None and target is None:
                return True

            if target is None:
                return False

            if root is None:
                return False

            if root.val == target.val:
                leftCheck = checkSubTree(root.left, target.left)
                rightCheck = checkSubTree(root.right, target.right)
                return leftCheck and rightCheck
            else:
                leftCheck = checkSubTree(root.left, target)
                rightCheck = checkSubTree(root.right, target)
                return leftCheck or rightCheck


        return checkSubTree(root, target)
        
