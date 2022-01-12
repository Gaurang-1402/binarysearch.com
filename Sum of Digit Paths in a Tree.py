# approach
# we maintain a global sum
# the key insight is to maintain the root vals as string numbers in the parameters
# of the function. There's only one case where we convert the digits string to a number
# it is when root left and right is None. That's when we finally convert the string to
# a numer and then add it to the globalSum

# any other case we add root val to digits and then make the left and right calls

# analysis
# we go through each node so the time taken is
# T = O(n)

# in case of a worst case scenario of a skewed tree, the space occupied is
# S = O(n)

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):

        if root is None:
            return 0

        globalSum = [0]
        def getSumInDDigitPath(root, digits):
            if root.left is None and root.right is None:
                digits += str(root.val)
                globalSum[0] += int(digits)
                return

            elif root.left is None:
                digits += str(root.val)
                getSumInDDigitPath(root.right, digits)
                return

            elif root.right is None:
                digits += str(root.val)
                getSumInDDigitPath(root.left, digits)
                return

            else:
                digits += str(root.val)
                getSumInDDigitPath(root.right, digits)
                getSumInDDigitPath(root.left, digits)
                return

        getSumInDDigitPath(root, "")
        return globalSum[0]
