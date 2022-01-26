# approach
# watch this: https://www.youtube.com/watch?v=wCc_nd-GiEc
# this is a classic dynamic programming memoization problem.

# we use dfs because we need to get the whole max path in one go
# then we need to save the length of this max path for each node on the
# way

# we also pass prevVal in the dfs as a praram. why? we only traverse if the given val
# is bigger than prevVal otherwise we're not increasing

# this way our dp will store all the max paths for any given r and c

# analysis
# if r and c are num of rows and num of cols, time complexity is
# T = O(r * c) or O(n) because each node is traversed at most once

# the max number of nodes on the call stack are
# S = O(r * c) or O(n)


class Solution:
    def solve(self, matrix):
        ROWS = len(matrix)
        COLS = len(matrix[0])

        dp = {} # maps (r, c) to LongestIncreasingPathAt(r, c)

        def dfs(r, c, prevVal): # passing prevVal is very important
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or matrix[r][c] <= prevVal:
                return 0

            if (r, c) in dp:
                return dp[(r, c)]

            maxPath = 1

            maxPath = max(maxPath, 1 + dfs(r + 1, c, matrix[r][c])) # the 1 + is VERY IMPORTANT it is the increment for any given successful traversal of path
            maxPath = max(maxPath, 1 + dfs(r, c + 1, matrix[r][c]))
            maxPath = max(maxPath, 1 + dfs(r - 1, c,  matrix[r][c]))
            maxPath = max(maxPath, 1 + dfs(r, c - 1,  matrix[r][c]))

            dp[(r, c)] = maxPath
            return maxPath

        for r in range(ROWS):
            for c in range(COLS):
                # make prevVal initially as -1 so that the first comparison is
                dfs(r, c, -1)

        return max(dp.values()) # time complexity of this line is O(n)
