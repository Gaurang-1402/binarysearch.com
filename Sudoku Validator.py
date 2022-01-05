import collections
rows = collections.defaultdict(set)
print(collections.defaultdict(set))

rows[5].add(3)
rows[5].add(5)
rows[2].add(1)
print(rows)
print(3 in rows[5])

cols = {4 : set(), 2: set()}
print(cols)

cols[4].add(2)
cols[4].add(5)
cols[2].add(1)
print(cols)
print(2 in cols[4])

# approach
# we need to map each row to a ds where we need O(k) lookup and need unique values for that row
# we need to map each col to a ds where we need O(k) lookup and need unique values for that col
# we need to map each section(size 3 by 3) to a ds where we need O(k) lookup and need unique values for that section(size 3 by 3)

# using a hash table where the key is row, col or (row, col) and value is a set() is a good idea to fulfill these requirements

# check the bounds to see if num is in bounds and

# for section part, watch this video: https://www.youtube.com/watch?v=TjFXEUCMqI8&t=619s
# dynamically fill up the hash tables and if you see repetition return false

# return true if no violation found


# analysis

# T = O(k) because the board will always be 9 by 9 or O(m * n)
# S = O(k) because the board will always be 9 by 9 or O(m * n)

class Solution:
    def solve(self, board):
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):

                if board[r][c] > 9 or board[r][c] < 1:
                    return False

                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3, c//3)]):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])

        return True

















