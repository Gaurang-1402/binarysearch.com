# analysis
# Time Complexity
# T = O(n) I visit every element at most twice and there are n of them

# Space Complexity
# S = O(n) I use auxiliary data structures using arrays and dictionaries each of size n

class Solution:
    def solve(self, nums, k):
        dp = [float("inf")] * len(nums)
        prefixSums = {}
        prefixSums[0] = -1
        res, total = float("inf"), 0

        for i in range(len(nums)):
            total += nums[i]
            dp[i] = dp[i - 1]
            if total - k in prefixSums:
                j = prefixSums[total - k] + 1
                if dp[j - 1] != float("inf") and j - 1 >= 0:
                    res = min(res, i - j + 1 + dp[j - 1])
                dp[i] = min(dp[i - 1], i - j + 1)
            prefixSums[total] = i

        return res if res != float("inf") else -1
