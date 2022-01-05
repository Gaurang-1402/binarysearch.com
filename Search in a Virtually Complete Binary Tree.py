# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, target):

        queue = []

        queue.append(root)

        while len(queue) != 0:
            curr = queue.pop(0)

            if curr.val == target:
                return True

            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)

        return False
