class Solution:
    def solve(self, nums, k):
        if not nums:
            return 0

        low, high = max(nums), sum(nums)

        while low < high:
            mid = (low + high) // 2

            days, curr = 1, 0
            for num in nums:
                if curr + num > mid:
                    days += 1
                    curr = num
                else:
                    curr += num

            if days > k:
                low = mid + 1
            else:
                high = mid

        return low
