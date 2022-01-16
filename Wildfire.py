# approach
# watch this: https://www.youtube.com/watch?v=y704fEOx0s0&t=612s
# we essentially use multisource bfs here because multiple trees will start burning the 1s

# analysis
# we go through each elem in the row and column of the matrix so if there are n elems
# time taken is
# T = O(n) or O(r * c)

# we save n elements in the queue so space consumed is
# S = O(n)

class Solution:
    def solve(self, matrix):

        if matrix == []:
            return 0

        ROWS = len(matrix)
        COLS = len(matrix[0])

        queue = deque()
        day = 0

        alive = 0

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 1:
                    alive += 1
                if matrix[r][c] == 2:
                    queue.append((r, c))


        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]


        while queue and alive > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:

                    row = r + dr
                    col = c + dc

                    if row < 0 or row >= ROWS or col < 0 or col >= COLS or matrix[row][col] != 1:
                        continue
                    matrix[row][col] = 2
                    queue.append((row, col))
                    alive -= 1
            day += 1

        return day if alive == 0 else -1
