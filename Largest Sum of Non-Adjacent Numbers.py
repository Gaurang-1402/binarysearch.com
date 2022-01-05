# approach
# This seems like a classic tabulation problem because of two reasons: it doesn’t make sense to compute all possibilities (memoization strategy) and because previous values contribute to current value, so it is useful to track previous values.

# The maximum sum possible at index i is the maximum value between the previous value in the table OR the value two indices behind + the value at index i in the nums array.

# The seed values cannot use the previous indices so you have to take care
# of all possible cases here. Since we can also get negative values, we have
# to include 0 in the max function of both the seed values. The 0th index
# can either have itself as a value or 0(if the val is -ve).
# Similarly the 1st index can either be itself or the previous val + nums at index 1 or 0 (if both other vals are -ve).
# Then we traverse from 2 because 0,1 are seed cases. And use the formula described. The last value should be the maximum one.

# analysis
# We are saving all max values in a table so space complexity is

# S = O(n)

# We go through each index so time complexity is

# T = O(n)



class Solution:
    def solve(self, nums):

        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        first = max(0, nums[0])

        second = max(0, nums[1], nums[0])

        for i in range(2, len(nums)):
            final = max(first + nums[i], second)
            first = second
            second = final

        return max(first, second)

        # table = [0 for num in range(len(nums))]
        #
        # table[0] = max(nums[0], 0)
        #
        # table[1] = max(nums[1], table[1] + nums[0], 0)
        #
        # for i in range(2, len(nums)):
        #     table[i] = max(table[i - 1], table[i - 2] + nums[i])
        #
        # return table[len(nums)-1]
