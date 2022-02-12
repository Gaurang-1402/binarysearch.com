# approach
# solution here: https://binarysearch.com/problems/Minimum-Number-of-Contiguous-K-Flips/solutions/3750258
# It can be solved in a greedy way based on two things:

# 1 - Flips are commutative and hence the order doesn't matter.
# For example: flips in ranges [1-5], [0-4] and [2-6] can be arranged in any order with the same impact on the position 3.

# 2 - Based on 1), no position should be flipped more than once. By contradiction, if that would be the case, one could rearrange flips so that flips at the same position happen one after the other hence canceling each other.

# A straightforward approach is to greedily check each value and if it's 1, flip next k elements (if possible). Repeat until we get all zeros or until it's impossible to flip.
# However, this is O(n∗k) since for every flip we may go next k places to update values.

# Better approach would be to keep left and right boundary when flipping. Then we count states as we go (line sweep).

# Implementation
# An additional detail is a way to flip states. It can be either number of flips at a given position mod 2, or we can leverage the fact that there are only two states (flipped or not), hence we can use x^1 to change from 0 to 1 and vice versa.

# analysis
# Time Complexity
# T = O(n) - A single pass through an array

# Space Complexity
# S = O(n) - An additional array to keep track of states

class Solution:
    def solve(self, nums, k):

        n = len(nums)

        # states[i] == 1 indicates that when considering the nums[i]
        # we should keep in mind that position is already flipped
        # it comes from handling nums[i-k] value
        states = [0] * n

        i = 0
        ans = 0
        # flip == 1 indicates that current position is flipped
        # it depends on states[i] and previous value
        flip = 0
        while i < n:
            # if states[i] is flipped at i-1 and and i-k it's actually not flipped
            flip ^= states[i]

            # decide if at position i we should make a flip or not
            if flip ^ nums[i] == 1: # flip and nums[i] are not the samee
                ans += 1
                # we just flipped our state
                flip ^= 1
                # if outside of array, it's impossible to flip
                if i + k > n:
                    return -1
                # record an event in future where flip is not valid
                if i + k < n:
                    states[i + k] ^= 1
            i += 1
        return ans


