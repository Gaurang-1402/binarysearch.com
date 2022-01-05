# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node, k):

        if node.next == None:
            return node.val

        curr = node
        currIdx = 0

        while currIdx < k:
            curr = curr.next
            currIdx += 1

        kthNode = node

        while curr.next != None:
            kthNode = kthNode.next
            curr = curr.next

        return kthNode.val
