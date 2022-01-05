class Solution:
    def solve(self, n):
        if n <= 1:
            return 1
        # Using DP table to store the Catalan numbers
        dp = [0] * (n + 1)

        # For 0 nodes, we can have just 1 BST (empty BST)
        dp[0] = 1

        # For 1 node, we can have just 1 BST
        dp[1] = 1

        # Formula discussed above
        # f(3) = (f(0) * f(3)) + (f(1) * f(2)) + (f(2) * f(1)) + (f(3) * f(0))
        for i in range(2, n + 1):

            lptr = 0
            rptr = i - 1

            while(lptr < i):
                dp[i] += dp[lptr] * dp[rptr]
                lptr += 1
                rptr -= 1

        return dp[n] % (10 ** 9 + 7)
