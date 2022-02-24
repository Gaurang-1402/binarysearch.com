# intuition
# important to recognize the moves that the knight can take.
# now that we know these positions, we need to draw a decision tree
# where each level is k.

# we can use memoization to remove repeated work

# implementation
# to account for probability, we can notice that there are 8 moves. Probability of each independent event
# is 1/8 so multiply it by the outcome of that move's event
#
# lastly memoize it with memo!

# analysis
# we go through each piece in n by n board so time complexity is
# T = O(n * n)

# space is dictated by the decision tree that has a height of k and worst case row
# of n length rows
# S = O(n * k)

class Solution:
    def solve(self, n, x, y, k):

        ROWS = n
        COLS = n

        memo = {}
        def dfs(x, y, k):

            if (x, y, k) in memo:
                return memo[(x, y, k)]

            if k == 0:
                # no moves left base case so we need the full 1/8 probability for this event
                return 1

            moves = [
                [2, 1],
                [-2, 1],
                [-2, -1],
                [2, -1],
                [-1, -2],
                [-1, 2],
                [1, 2],
                [1, -2]
            ]

            prob = 0

            for move in moves:
                dx, dy = move

                # only make a move if (x + dx) and (y + dy) in the range
                if 0 <= (x + dx) < ROWS and 0 <= (y + dy) < COLS:
                    # multiply each move in dfs by 1/8 as each event is independent
                    prob += (1/8 * dfs(x + dx, y + dy, k - 1))

            memo[(x, y, k)] = prob

            return memo[(x, y, k)]

        return int(100 * dfs(x, y, k))
