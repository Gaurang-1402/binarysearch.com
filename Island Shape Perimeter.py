# approach

# important to realize that perimeter increases only if we are out of bounds in 4 directions or is
# matrix[r][c] == 0

# bfs through the matrix graph and ensure we don't visit a node we have already visited
# mark nodes as visited as soon as you pop them out or add them to visited if not

# since we only have one connected component we can directly return

# analysis
# go through each node once so if r is rows and c is columns, time complexity is
# T = O(r*c)

# space complexity is the length of the queue so in case we have all 1s,
# S = O(r*c)

class Solution:
    def solve(self, matrix):

        ROWS = len(matrix)
        COLS = len(matrix[0])

        def bfsExplore(r, c, matrix):
            visited = set()
            queue = collections.deque()
            perimeter = 0

            queue.append((r, c))

            while len(queue):
                currR, currC = queue.popleft()

                if (currR, currC) in visited:
                    continue

                visited.add((currR, currC))
                directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

                for direction in directions:
                    dr, dc = direction

                    newR = dr + currR
                    newC = dc + currC

                    if newR < 0 or newR >= ROWS or newC < 0 or newC >= COLS or matrix[newR][newC] == 0:
                        perimeter += 1
                    else:
                        queue.append((newR, newC))


            return perimeter


        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 1:
                    return bfsExplore(r, c, matrix)
