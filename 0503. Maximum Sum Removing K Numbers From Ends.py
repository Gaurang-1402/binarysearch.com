class Solution:
    def solve(self, nums, k):
        window = sum(nums[:k])
        ans = window
        for i in range(1, k + 1):
            window -= nums[k - i]
            window += nums[-i]
            ans = max(ans, window)
        return ans

