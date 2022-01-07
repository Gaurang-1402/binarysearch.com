# approach

# the trick is to check if two binary trees are identical. Both the binary trees to be checked are the trees
# given in the question. However, traversing the trees will always be opposite.

# If we traverse left in one tree
# we traverse right in the other tree and see if they are identical.
# to check if trees are identical, check if root
# vals are the same. if yes, check if left and right is the same.

# there are two base cases to consider. if one of the roots of the tree is none or if both roots of the trees are
# none in either case return based on the symmetric nature


# analysis
# since we go through each val in the root twice, time complexity is
# T = O(n)

# in case of a skewed tree, space complexity is
# S = O(n)

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):

        def isTreeSymmetric(root1, root2):
            if root1 is None and root2 is None:
                return True
            elif root1 is None or root2 is None:
                return False

            else:
                if root1.val == root2.val:
                    oneCheck = isTreeSymmetric(root1.left, root2.right)
                    twoCheck = isTreeSymmetric(root1.right, root2.left)

                    return oneCheck and twoCheck
                else:
                    return False


        return isTreeSymmetric(root, root)

