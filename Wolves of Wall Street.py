class Solution:
    def solve(self, prices):
        max_profit = 0
        for i in range(1, len(prices)):
            change = prices[i] - prices[i - 1]
            if change > 0:
                max_profit += change
        return max_profit
