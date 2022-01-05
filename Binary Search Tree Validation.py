# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# approach:

# it is important to notice that at any stage in the recursive calls,
# your val has to be between a lower and upper limit
# The upper limit starts with inf and lower limit starts with -inf
# when you go left upper limit is val and maintain the parent lowerlimit
# when you go right lower limit is val and you maintain parent lowerlimit


class Solution:
    def solve(self, root):
        # edge cases

        if root is None:
            return True

        def bstValidation(root, lowerLimit, upperLimit):
            if root.left is None and root.right is None:
                return lowerLimit < root.val < upperLimit

            elif root.left is None:
                rightCheck = bstValidation(root.right, root.val, upperLimit)
                return rightCheck and lowerLimit < root.val < upperLimit

            elif root.right is None:
                leftCheck = bstValidation(root.left, lowerLimit, root.val)
                return leftCheck and lowerLimit < root.val < upperLimit

            else:
                return bstValidation(root.left, lowerLimit, root.val) and bstValidation(root.right, root.val, upperLimit) and lowerLimit < root.val < upperLimit

        return bstValidation(root, float("-inf"), float("inf"))
