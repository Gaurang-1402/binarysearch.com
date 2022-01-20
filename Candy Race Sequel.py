# approach
# read the approach here: https://binarysearch.com/problems/Candy-Race-Sequel/solutions/3416998

# analysis
# Time Complexity
# T = O(n) since the cache will not recompute and O(2n) is O(n) ;) -> turn is either True or False

# Space Complexity
# S = O(n) again this is the space used by the cache... O(2n)


class Solution:
    def solve(self, nums):
        @functools.cache
        def go(i, turn):
            if i == len(nums):
                return 0

            if turn:  # maximize!
                res = float("-inf")
                cur_sum = 0
                for j in range(i, min(i + 3, len(nums))):
                    cur_sum += nums[j]
                    res = max(res, cur_sum + go(j + 1, not turn))
            else:  # minimize
                res = float("inf")
                # no cur_sum because you are minimizing
                # my next move!
                for j in range(i, min(i + 3, len(nums))):
                    res = min(res, go(j + 1, not turn))
            return res

        return go(0, True) > sum(nums) // 2
