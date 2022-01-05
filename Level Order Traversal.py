# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def solve(self, root):

        queue = []
        levelOrder = []
        queue.append(root)

        while len(queue) != 0:
            currNode = queue.pop(0)

            levelOrder.append(currNode.val)

            if currNode.left is not None:
                queue.append(currNode.left)

            if currNode.right is not None:
                queue.append(currNode.right)



        return levelOrder
        
