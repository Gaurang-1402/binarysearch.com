# approach
# this is the merge step in merge sort algorithm.
# maintain 2 pointers one on firstLst and two on secondLst
# while both of them and smaller than respective lists
# add the item that is smaller between the two lists and increment
# the appropriate pointer. INCREMENTING IS VERY IMPORTANT

# if any of the pointers reaches the end of the respective lists,
# you can add elements stored in the non completed lists

# analysis
# we maintain pointers on two lists of size n and m and traverse through both of them
# T = O(n + m)

# we store n + m elements in a new list. So space complexity is
# S = O(n + m)

class Solution:
    def solve(self, a, b):

        p1 = 0
        p2 = 0

        finalLst = []

        while p1 < len(a) and p2 < len(b):
            if a[p1] <= b[p2]:
                finalLst.append(a[p1])
                p1 += 1
            else:
                finalLst.append(b[p2])
                p2 += 1

        while p1 < len(a):
            finalLst.append(a[p1])
            p1 += 1

        while p2 < len(b):
            finalLst.append(b[p2])
            p2 += 1

        return finalLst
