# approach

# key thing to realize is that the lowest common ancestor is one that
# has both the values in its left and right subtree
# but what if root itself has a value a or b then we can safely return root

# on any given recursive call, we just need to find one of the
# roots with vals a or b.

# in a case where we have a and b in left and right subtree, we have found LCA

# analysis
# we go through each node so time complexity is
# T = O(n)

# in case we get a skewed tree, space complexity is
# S = O(n)

class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def solve(self, root, a, b):

        def getLowestCommonAncestor(root, a, b):

            if root is None:
                return None

            # finding left and right sub tree
            leftLca = getLowestCommonAncestor(root.left, a, b)
            rightLca = getLowestCommonAncestor(root.right, a, b)

            # if node is a or b then return that node to the node
            if root.val == a or root.val == b:
                return root

            # if both left and right subtree are not none then return root
            if leftLca and rightLca:
                return root

            # if one sub tree is None and one sub tree is not None
            if leftLca:
                return leftLca

            if rightLca:
                return rightLca

            return None

        return getLowestCommonAncestor(root, a, b).val



