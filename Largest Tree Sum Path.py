# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def solve(self, root):

        if root is None:
            return 0

        resultFromTriangle = [0]

        def explore(root):
            if root is None:
                return 0

            leftHeightSum = explore(root.left)
            rightHeightSum = explore(root.right)

            leftHeightSum = max(leftHeightSum, 0)
            rightHeightSum = max(rightHeightSum, 0)

            maxHeightSum = max(leftHeightSum, rightHeightSum)

            currentTriangleSum = leftHeightSum + rightHeightSum + root.val
            resultFromTriangle[0] = max(resultFromTriangle[0], currentTriangleSum)

            return root.val + maxHeightSum

        explore(root)
        return resultFromTriangle[0]
