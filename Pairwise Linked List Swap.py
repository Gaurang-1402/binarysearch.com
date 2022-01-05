# approach
# maintain 3 pointers - prev (starting with None), mid(starting with node) and
# front (starting with node.next)
# we have to make mid front and front mid and connect prev from mid to front
# be careful in the reassignment of pointers
# prev should be reassigned before mid is

# analysis
# T(n) = O(n)
# S(n) = O(k)


class LLNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class Solution:
    def solve(self, node):
        # edge cases

        if node is None or node.next is None:
            return node


        head = node.next
        front = node.next
        mid = node
        prev = None

        while front is not None:

            mid.next = front.next
            front.next = mid
            if prev is not None:
                prev.next = front

            if mid.next is not None:
                front = mid.next.next
                prev = mid
                mid = mid.next

            else:
                front = None

        return head
