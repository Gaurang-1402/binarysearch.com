# approach
# We go dfs through a node only if its value is 1. While dfsing, we increment the area (starting with 1 because of currNode's value)
# to keep track of area in the 4 directions covered
# we also mark visited nodes so we don't revisit them

# finally in the outer traversal, we keep track of the maximum area

# analysis
# since we go through each node in the grid in the worst case scenario where entire grid is composed of 1s,
# T = O(n) where n is number of nodes

# we store at most n nodes in the stack frames leading the space complexity to become
# S = O(n)

class Solution:
    def solve(self, matrix):

        ROWS = len(matrix)
        COLS = len(matrix[0])

        def explore(r, c, visited):

            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return 0

            if (r, c) in visited:
                return 0

            visited.add((r, c))

            if matrix[r][c] == 0:
                return 0

            currMaxArea = 1

            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

            for direction in directions:
                dr, dc = direction
                currMaxArea += explore(r + dr, c + dc, visited)

            return currMaxArea

        visited = set()
        maxArea = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and matrix[r][c] == 1:
                    maxArea = max(explore(r, c, visited), maxArea)

        return maxArea

