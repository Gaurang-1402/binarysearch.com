# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):

        if node == None:
            return True

        def lenOfList(node):

            listLen = 1

            curr = node

            while curr.next is not None:
                curr = curr.next
                listLen += 1

            return listLen

        def reverseList(node, k):
            prev, curr = None, node

            # why make it start from 0?
            # firstHalf is initially starting on prev
            # which starts from None so nodeCount should be 0 until we are one less than k (len of list)
            # curr is the secondHalf Head or the middle node in palindrome which we deal with later
            #
            nodeCount = 0

            while nodeCount < k:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode
                nodeCount += 1

            return prev, curr

        listLen = lenOfList(node)

        if listLen == 1:
            return True

        if listLen % 2 == 0:
            firstHalf, secondHalf= reverseList(node, listLen // 2)
        else:
            firstHalf, secondHalfPlusMiddle = reverseList(node, (listLen -1) // 2)
            secondHalf = secondHalfPlusMiddle.next

        while firstHalf is not None and secondHalf is not None:
            if firstHalf.val != secondHalf.val:
                return False
            firstHalf = firstHalf.next
            secondHalf = secondHalf.next

        return True







