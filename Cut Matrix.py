import defaultdict
from functools import lru_cache
class Solution:
    def solve(self, matrix, k):
        MOD = 10 ** 9 + 7

        m, n = len(matrix), len(matrix[0])
        counts = defaultdict(int)
        for i in range(m)[::-1]:
            for j in range(n)[::-1]:
                counts[(i, j)] = (
                    counts[(i + 1, j)] + counts[(i, j + 1)] - counts[(i + 1, j + 1)] + matrix[i][j]
                )

        # number of ways for matrix[x:][y:] with c cuts remaining
        @lru_cache(None)
        def f(x, y, c):
            count = counts[(x, y)]
            if c == 0:
                return 1 if count > 0 else 0

            ans = 0
            for i in range(x + 1, m):
                if 0 < counts[(i, y)] < count:
                    ans += f(i, y, c - 1)
            for j in range(y + 1, n):
                if 0 < counts[(x, j)] < count:
                    ans += f(x, j, c - 1)
            # print(x, y, c, ans)
            return ans % MOD

        return f(0, 0, k - 1)
