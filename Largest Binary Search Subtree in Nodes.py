
# approach

# you cannot use the classic bst checker approach. key insight to realize is
# that there are multiple cases to be resolved


# analysis
# T = O(n)

# S = O(n)

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):

        def findLargestBst(root):
            if root.left is None and root.right is None:
                return (root, 1)

            elif root.left is None:
                largestRhsBst, largestRhsBstSize = findLargestBst(root.right)

                if largestRhsBst == root.right and root.val < root.right.val:
                    return (root, largestRhsBstSize + 1)
                else:
                    return (largestRhsBst, largestRhsBstSize)

            elif root.right is None:
                largestLhsBst, largestLhsBstSize = findLargestBst(root.left)

                if largestLhsBst == root.left and root.left.val < root.val:
                    return (root, largestLhsBstSize + 1)
                else:
                    return (largestLhsBst, largestLhsBstSize)
            else:
                largestRhsBst, largestRhsBstSize = findLargestBst(root.right)
                largestLhsBst, largestLhsBstSize = findLargestBst(root.left)

                if largestLhsBst == root.left and largestRhsBst == root.right and root.left.val < root.val < root.right.val:
                    return (root, largestRhsBstSize + largestLhsBstSize + 1)
                else:
                    return (largestRhsBst, largestRhsBstSize) if largestRhsBstSize > largestLhsBstSize else (largestLhsBst, largestLhsBstSize)

        return findLargestBst(root)[0]
