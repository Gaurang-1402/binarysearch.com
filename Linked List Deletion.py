 class LLNode:
     def __init__(self, val, next=None):
         self.val = val
         self.next = next
class Solution:
    def solve(self, node, target):

        dummy = LLNode(None, node)
        prev, curr = dummy, node

        while curr is not None:
            if curr.val == target:
                prev.next = curr.next
                curr = prev.next
            else:
                prev = curr
                curr = curr.next

        return dummy.next







