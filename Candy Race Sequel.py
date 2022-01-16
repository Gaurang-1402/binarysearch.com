# still to be commented on
class Solution:
    def solve(self, nums):
        n = len(nums)
        dp = [0, 0, 0]

        for i in range(n - 1, -1, -1):
            profit = -math.inf
            candy_sum = 0

            for j in range(i, min(i + 3, n)):
                candy_sum += nums[j]
                profit = max(profit, candy_sum - dp[j - i])

            dp[:] = [profit, dp[0], dp[1]]
    
        return dp[0] > 0
