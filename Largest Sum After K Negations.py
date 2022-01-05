
# approach
# the goal is to maximize the sum
# the constraint is to use k operations

# Greedy approach
# we first sort the list
# then we negate each of the elems that are negative and decrement k
# if k is even after this, we can just return sum(nums) (even negations cancel out)
# now if we have k with an odd number, we return the sum(nums) - 2 * min(nums)
# because we want to negate the minimum val in nums

# but why - 2 * min(nums) and not just -1* min(nums)
# because we want to decrement the sum(num) min(num) vals back
# and not just remove min(nums) from the sum(num)
# think of it in terms of a number line

# analysis
# T(n) = O(nlogn) due to sorting
# S(n) = O(k) as no other data structure used to store


class Solution:

    def solve(self, nums, k):
        nums.sort()

        index = 0

        while index < len(nums) and nums[index] < 0 and k > 0:
            nums[index] = -nums[index]
            k -= 1
            index += 1

        return sum(nums) if k % 2 == 0 else sum(nums) - 2 * min(nums)

