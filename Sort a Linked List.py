 class LLNode:
     def __init__(self, val, next=None):
         self.val = val
         self.next = next
class Solution:
    def solve(self, node):

        # merge sort

        if node is None or node.next is None:
            return node

        # get mid
        left = node

        right = self.getMid(node)

        temp = right.next
        right.next = None
        right = temp

        # sort
        left = self.solve(left)
        right = self.solve(right)

        # merge
        merged = self.merge(left, right)

        return merged


    def merge(self, node1, node2):

        curr = LLNode(None)
        dummy = LLNode(None, curr)

        while node1 and node2:
            if node1.val < node2.val:
                curr.next = node1
                node1 = node1.next
                curr = curr.next
            else:
                curr.next = node2
                node2 = node2.next
                curr = curr.next


        while node1:
            curr.next = node1
            node1 = node1.next
            curr = curr.next

        while node2:
            curr.next = node2
            node2 = node2.next
            curr = curr.next

        return dummy.next.next


    def getMid(self, node):
        slow, fast = node, node.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


