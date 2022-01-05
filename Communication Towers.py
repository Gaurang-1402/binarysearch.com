class Solution:
    def solve(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        visited = set()
        numOfGroups = 0

        def dfs(row, col, visited):

            if row >= rows or col >= cols or row < 0 or col < 0:
                return None

            if (row, col) in visited:
                return None

            visited.add((row, col))

            if matrix[row][col] == 0:
                return None

            for r in range(row + 1, rows):
                dfs(r, col, visited)

            for r in range(row, -1, -1):
                dfs(r, col, visited)

            for c in range(col + 1, cols):
                dfs(row, c, visited)

            for c in range(col, -1, -1):
                dfs(row, c, visited)

            return None

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and matrix[r][c] == 1:
                    dfs(r, c, visited)
                    numOfGroups += 1


        return numOfGroups



