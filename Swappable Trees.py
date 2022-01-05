# approach

# Intuition
# Since we have to focus on swapping left and right, we can get the level order traversals of the list. This makes it so that for any index, i, in levelOrderLstRoot0, the corresponding i + 1 or i -1 in levelOrderLstRoot1 should be the val at i. If not then we return false. Also, if the lists aren't the same size, we can return False.

# Implementation
# We define a function to get the level order traversal of the two roots. Then convert the levelOrderTraversal lists with roots to lists with vals at those roots. We ensure the lengths of these lists are the same and then go through each index in levelOrderTraversalRoot0 and check if indices i, i + 1 or i - 1 in levelOrderTraversalRoot1 get us the val. If not we return false.

# Please upvote if you liked the explanation!

# analysis

# Time Complexity
# T = O(n) we go through each node in the two roots provided. In case they have significantly different number of nodes, we may get time complexity of \mathcal{O}(m + n)O(m+n)

# Space Complexity
# S = O(n) we save the level order traversals of the root which occupies 2n space and we drop the constant. In case they have significantly different number of nodes, we may get space complexity of \mathcal{O}(m + n)O(m+n)

# class Tree:


class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def solve(self, root0, root1):

        def levelOrderTraversal(root):

            queue = [root]

            levelOrderLst = []

            while len(queue) > 0:
                curr = queue.pop(0)

                levelOrderLst.append(curr)

                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)

            return levelOrderLst


        levelOrderLstRoot0 = [root.val for root in levelOrderTraversal(root0)]

        levelOrderLstRoot1 = [root.val for root in levelOrderTraversal(root1)]

        if len(levelOrderLstRoot0) != len(levelOrderLstRoot1):
            return False

        for i, val in enumerate(levelOrderLstRoot0):
            if levelOrderLstRoot1[i] != val:
                if i > 0 and levelOrderLstRoot1[i - 1] == val:
                    continue
                if i + 1 < len(levelOrderLstRoot1) and levelOrderLstRoot1[i + 1] == val:
                    continue
                return False

        return True


