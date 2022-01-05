# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):

        if root.left is None and root.right is None:
            return 1


        def dfsUniValue(root):
            if root.left is None and root.right is None:

                return (True, 1)

            elif root.left is None:
                isUniValue, uniValueCount = dfsUniValue(root.right)
                if isUniValue and root.val == root.right.val:
                    uniValueCount += 1

                if isUniValue and root.val == root.right.val:
                    return (True, uniValueCount)
                else:
                    return (False, uniValueCount)

            elif root.right is None:
                isUniValue, uniValueCount = dfsUniValue(root.left)
                if isUniValue and root.val == root.left.val:
                    uniValueCount += 1

                if isUniValue and root.val == root.left.val:
                    return (True, uniValueCount)
                else:
                    return (False, uniValueCount)

            else:
                isUniValueLeft, uniValueCountLeft = dfsUniValue(root.left)
                isUniValueRight, uniValueCountRight = dfsUniValue(root.right)

                uniValueCount = uniValueCountLeft + uniValueCountRight

                if isUniValueLeft and isUniValueRight and root.val == root.right.val and root.left.val == root.val:
                    uniValueCount += 1
                    return True, uniValueCount

                else:
                    return False, uniValueCount
        isRootUnique, uniValueCount = dfsUniValue(root)
        return uniValueCount

                
