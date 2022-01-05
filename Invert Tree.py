# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def solve(self, root):

        def helper(root):
            if root is None:
                return root

            left= helper(root.left)
            right= helper(root.right)
            root.left = right
            root.right = left

            return root
        return helper(root)

        # if root is None:
        #     return None

        # if root.left is None and root.right is None:
        #     return

        # elif root.left is None:
        #     root.left = root.right
        #     root.right = None
        #     self.solve(root.right)

        # elif root.right is None:
        #     root.left = root.right
        #     root.right = None
        #     self.solve(root.left)

        # else:
        #     leftRoot = root.left
        #     root.left = root.right
        #     root.right = leftRoot
        #     self.solve(root.left)
        #     self.solve(root.right)

        # return root


        
