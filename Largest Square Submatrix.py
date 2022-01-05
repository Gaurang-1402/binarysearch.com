class Solution:
    def solve(self, matrix):


        ROWS, COLS = len(matrix), len(matrix[0])

        cache = {} # map (r, c) -> max len of square starting at r, c as top left

        def traverser(r, c):
            if r >= ROWS or c >= COLS:
                return 0

            if (r, c) not in cache:

                down = traverser(r + 1, c)
                right = traverser(r, c + 1)
                diagonal = traverser(r + 1, c + 1)


                cache[(r, c)] = 0
                if matrix[r][c] == 1:
                    cache[(r, c)] = 1 + min(down, right, diagonal)

            return cache[(r, c)]


        traverser(0, 0)

        return max(cache.values()) ** 2



        
