# approach
# the hints in the question are that the matrix is sorted both
# row and col wise

# since we need time complexity of O(m + n),
# we can only go through n elems rowwise
# we can only go through m elems colwise

# now to use these facts, we start from top right corner
# and go right or down depending on the currElem compared to target

# if we find the elem, we return true

# if the loop we are in is quit we return false

# analysis

# since
# we can only go through n elems rowwise once
# we can only go through m elems colwise once
# time complexity is
# T = O(n)

# we don't use any extra space so space complexity is
# S = O(k)

class Solution:
    def solve(self, matrix, target):

        ROWS = len(matrix)
        COLS = len(matrix[0])

        r = 0
        c = COLS - 1

        while r < ROWS and c >= 0:
            currElem = matrix[r][c]

            if currElem == target:
                return True
            elif currElem > target:
                c -= 1
            else:
                r += 1

        return False
