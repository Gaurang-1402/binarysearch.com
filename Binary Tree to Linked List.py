# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, root):

        if root == None:
            return None

        def createLinkedList(root, listSoFar):
            if root.left is None and root.right is None:
                listSoFar.next = LLNode(root.val)
                listSoFar = listSoFar.next
                return listSoFar

            elif root.left is None:
                listSoFar.next = LLNode(root.val)
                listSoFar = listSoFar.next
                listSoFar = createLinkedList(root.right, listSoFar)
                return listSoFar

            elif root.right is None:
                listSoFar = createLinkedList(root.left, listSoFar)
                listSoFar.next = LLNode(root.val)
                listSoFar = listSoFar.next
                return listSoFar

            else:
                listSoFar = createLinkedList(root.left, listSoFar)
                listSoFar.next = LLNode(root.val)
                listSoFar = listSoFar.next
                listSoFar= createLinkedList(root.right, listSoFar)
                return listSoFar

        dummy = LLNode(0)
        createLinkedList(root, dummy)
        return dummy.next
