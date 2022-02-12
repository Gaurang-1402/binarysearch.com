# approach
# watch this video to understand: https://www.youtube.com/watch?v=2wCShtvcP0Q

# probability of picking any num from [1, 2, ... maxJump] ==> 1/(maxJump) due to even distribution

# Let's take an example
# n = 21
# threshold = 18
# maxJump = 6

# Solution = Probability(n) + Probability(n-1) + .... P(threshold)
# final sum is in the range [threshold, ..., n]

# DP[i] --> probability of reaching number i

# analysis
# time taken is O(n) because we go through at most n numbers in the for loop
# T = O(n)

# space
# S = O(n) because we save n elements at most

class Solution:
    def solve(self, n, threshold, maxJump):

        if threshold == 0 or n >= threshold + maxJump:
            # edge cases where we're certain probability of 1
            return 1.0

        dp = [0.0 for _ in range(n+1)]

        dp[0] = 1.0

        runningSum = dp[0]

        result = 0.0

        for i in range(1, n+1):
            dp[i] = runningSum/maxJump

            if i < threshold:
                runningSum += dp[i]

            else:
                result += dp[i]

            if i - maxJump >= 0:
                runningSum -= dp[i - maxJump]

        return result

