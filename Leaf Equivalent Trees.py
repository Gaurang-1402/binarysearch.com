# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root0, root1):

        def getLeafsOfTree(root):
            stack = []
            leafList = []

            stack.append(root)

            while (len(stack) != 0):
                currNode = stack.pop()
                if currNode.left is None and currNode.right is None:
                    leafList.append(currNode.val)

                if currNode.left is not None:
                    stack.append(currNode.left)

                if currNode.right is not None:
                    stack.append(currNode.right)


            return leafList

        leavesOfRoot0 = getLeafsOfTree(root0)
        leavesOfRoot1 = getLeafsOfTree(root1)

        return leavesOfRoot0 == leavesOfRoot1
