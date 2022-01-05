
# approach:
# We go through the list backwards.
# At each step, we keep track of numbers already seen in sorted order.
# To find how many numbers are smaller than the current number, we binary search in the sorted list.

# Example:
# lst = [1,5,3,4]
# When we are looking at the 5, our sorted list is [3,4].
# Bisect_left(5) gives us the leftmost index where we could insert 5 which is index 2.
# This is the same as the number of elements smaller than 5.

# However, binarysearch_com is kind enough to include the sortedcontainers library which has SortedList()
# Both the add and bisect_left methods have time complexity of O(logn)
# PS: The bisect_left method is the binary_search algorithm

# analysis:
# Time: O(nlogn) - for each element, we do a O(log n) binary search and a O(log n) insertion.
# Space: O(n) - we store each element in the sorted list.

from sortedcontainers import SortedList

class Solution:


    def solve(self, lst):
        # https://www.geeksforgeeks.org/python-sorted-containers-an-introduction/
        srt = SortedList()

        # add(value) : A function that takes one element as parameter and inserts it into the list by
        # maintaining sorted order. Runtime Complexity: O(log(n))

        # discard(value): Remove value from sorted list if it is a member. If value is not a member, do nothing.
        # Runtime complexity: O(log(n)).

        ans = [0] * len(lst)
        for i, x in enumerate(reversed(lst), 1):

            # https://www.geeksforgeeks.org/binary-search-bisect-in-python/?ref=lbp
            r = srt.bisect_left(x)
            ans[-i] = r
            srt.add(x)
        return ans

        # # bruteforce

        # smallerElems = []

        # for i, num in enumerate(lst):
        #     count = 0
        #     for j in range(i, len(lst)):
        #         if lst[j] < num:
        #             count += 1

        #     smallerElems.append(count)

        # return smallerElems
