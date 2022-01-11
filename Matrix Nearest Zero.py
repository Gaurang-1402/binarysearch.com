# approach
# we use multisource bfs here. why? watch this for an explanation: https://www.youtube.com/watch?v=e69C6xhiSQE
# basically add all the nodes starting with value 0 are added to the queue first
# we simultaneously start bfs from all of them

# how do we ensure min distance is being recorded? we never visit a node again(using visit set) so the first time we reach it,
# the distance is entered

# on rach iteration of the bfs loop, we have a new layer of nodes in the queue and we set the matrix[r][c] value
# of all of them as the currDistance being maintained right now

# analysis
# we go through each value in the grid so time complexity is
# T = O(r * c)

# we mutate in place and don't use any extra space so space complexity is
# S = O(k)

class Solution:
    def solve(self, matrix):

        ROWS = len(matrix)
        COLS = len(matrix[0])

        def checkBounds(r, c):
            if (r, c) in visited:
                return False

            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return False
            visited.add((r, c))
            queue.append((r, c))
            return True

        visited = set()
        queue = collections.deque()

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    visited.add((r, c))
                    queue.append((r, c))

        distance = 0
        while len(queue):
            n = len(queue)
            for node in range(n):
                r, c = queue.popleft()

                # for layer 0 where we do need 0s we will set distance as 0
                matrix[r][c] = distance

                directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

                for direction in directions:
                    dr, dc = direction
                    checkBounds(r + dr, c + dc)

            distance += 1

        return matrix



        
