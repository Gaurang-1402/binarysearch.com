# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):

        def recursiveSame(root):

            if root.left is None and root.right is None:
                return True

            elif root.left is None:
                rightCheck = recursiveSame(root.right)
                return rightCheck and root.right.val == root.val

            elif root.right is None:
                leftCheck = recursiveSame(root.left)
                return leftCheck and root.left.val == root.val


            else:
                rightCheck = recursiveSame(root.right)
                leftCheck = recursiveSame(root.left)
                return leftCheck and rightCheck and root.left.val == root.val and root.right.val == root.val

        return recursiveSame(root)


        
