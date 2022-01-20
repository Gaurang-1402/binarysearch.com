# approach
# we maintain prefixSums and suffixSums
# suffixSums starts from the full sum of nums.
# prefixSums starts from 0
# if at any stage they are equal, we can return that index

# analysis
# time taken due to the iteration of nums is
# T = O(n)

# space occupied is constant so space complexity is
# S = O(k)

class Solution:
    def solve(self, nums):
        suffixSums = sum(nums)
        prefixSums = 0

        for i, num in enumerate(nums):
            # we decrement from suffixSums because at index i
            # the num is already included in suffixSums which we need to remove
            suffixSums -= x
            if suffixSums == prefixSums:
                return i
            prefixSums += x

        return -1

