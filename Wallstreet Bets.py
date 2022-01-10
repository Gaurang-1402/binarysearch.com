# approach

# The idea is simple, but a bit tricky. We use a monoqueue, and make sure that any values in the stack are < the current value.
# We only pop from the stack when the current price is > the top of the stack.
# This is basically when we can take a profit. We rewrite the distance from the current profit stock to where we original saw the stock.
# Since the goal is just to take any profit (not best profit), we can greedily pop from our stack.

# 1) Go through all prices
# 2) Check the stack for possible profit
# 3) If we have profit, pop off and rewrite that value into ans, the the distance from the current idx and from where we saw the value

# analysis
# Time Complexity
# T = O(n), we need to visit every value in our price list

# Space Complexity
# S = O(n), worst case, the entire list ends up on the stack

class Solution:
    def solve(self, prices):

        firstProfit = [0 for price in prices]

        stack = []

        for i, price in enumerate(prices):
            while len(stack) and price > stack[-1][1]:
                j, prevPrice = stack.pop()
                firstProfit[j] = i - j
            stack.append((i, price))

        return firstProfit

        # bruteforce

        # for i, price in enumerate(prices):

        #     profitPossible = False
        #     for nextPriceIdx in range(i, len(prices)):
        #         if prices[nextPriceIdx] > price:
        #             firstProfit.append(nextPriceIdx - i)
        #             profitPossible = True

        #             break

        #     if not profitPossible:
        #         firstProfit.append(0)

        # return firstProfit
