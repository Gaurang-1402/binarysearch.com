# approach
# this problem uses the unbounded knapsack approach. Watch this video to understand: https://www.youtube.com/watch?v=Mjy4hd2xgrs&t=1134s

# analysis for tabulation approach
# Time Complexity
# T = O(n∗k): We are iterating over all values of n and k and in a nested loop.

# Space Complexity
# S = O(k): We are using an array of size k+1 to store the ways to reach that state.

class Solution:
    # memoization approach
    def solve(self, nums, k):

        uniqueCombs = [0]

        def explore(nums, k, index, memo):

            if k < 0:
                return 0

            if k == 0:
                return 1

            if index == len(nums):
                return 0

            if (index, k) in memo:
                return memo[(index, k)]

            pickMe = explore(nums, k - nums[index], index, memo)
            skipMe = explore(nums, k, index + 1, memo)

            memo[(index, k)] = pickMe + skipMe
            return memo[(index, k)]

        return explore(nums, k, 0, {})

    # tabulation approach
    def solve(self, nums, k):
        dp = [0] * (k + 1)
        dp[0] = 1

        for i in range(0, len(nums)):

            for j in range(nums[i], k + 1):

                dp[j] += dp[j - nums[i]]

        return dp[k]
