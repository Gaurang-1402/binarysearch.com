# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):

        currNode = node
        lenOfList = 0
        while currNode is not None:
            lenOfList += 1
            currNode = currNode.next

        return lenOfList

            
