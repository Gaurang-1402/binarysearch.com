# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root0, root1):
        if root0 is None and root1 is None:
            return True

        else:
            if root0 and root1:
                if root0.val == root1.val:
                    checkLeft = self.solve(root0.left, root1.left)
                    checkRight = self.solve(root0.right, root1.right)
                    return checkLeft and checkRight
                else:
                    return False
            else:
                return False


        
