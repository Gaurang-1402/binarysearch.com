# approach
# read the question carefully and it becomes obvious that we have to eliminate any islands that are connected to
# the boundary of the grid. Only islands that are ENTIRELY surrounded by 0s are considered islands

# the first thing we do is we mark all 1s around the four edges as visited without changing the count
# now that the borders (and surrounding 1s) are all visited, we can go through each 1 node in inner grid
# and dfs through it to find an island. Each time we encounter a 1 not visited, we increment the count because
# this is a 1 in the middle of water

# analysis
# since we visit each node at least once in the worst case, time complexity is
# T = O(n)

# the visited set holds n nodes at most so space complexity is
# S = O(n)

class Solution:
    def solve(self, matrix):

        ROWS = len(matrix)
        COLS = len(matrix[0])

        visited = set()

        def explore(r, c):

            if (r, c) in visited:
                return

            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return

            visited.add((r, c))

            if matrix[r][c] == 0:
                return
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

            for direction in directions:
                dr, dc = direction
                explore(r + dr, c + dc)

            return

        for r in range(ROWS):
            if (r, 0) not in visited:
                explore(r, 0)

        for r in range(ROWS):
            if (r, COLS-1) not in visited:
                explore(r, COLS-1)

        for c in range(COLS):
            if (0, c) not in visited:
                explore(0, c)

        for c in range(COLS):
            if (ROWS-1, c) not in visited:
                explore(ROWS-1, c)

        count = 0
        for r in range(1, ROWS - 1):
            for c in range(1, COLS - 1):
                if (r, c) not in visited and matrix[r][c] == 1:
                    explore(r, c)
                    count += 1

        return count
        
