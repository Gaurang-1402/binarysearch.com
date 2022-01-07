# approach
# The solution here is to use a running prefix sum. The intuition for this algorithm comes down to several things:

# If you write the brute force solution (or simulate it), you'd basically be going through each continuous subarray from each position and summing them up. You'd quickly realize you're computing the same sum over and over again (because they are overlapping, for example a[3] = **a[0] + a[1]** + a[2] but a[2] = **a[1] + a[0]** (shared elements are surrounded by *)
# Therefore, we need a technique to calculate the sum between two indexes (i.e., a subarray) quickly. This technique is called prefix sums.
# Once we have this technique, now to get the count, the key question to ask is: "How many subarray sums can I remove from my running window so far, such that it adds to the target"?
# Now - you need a mechanism to store the running subarray sums you encounter to ask yourself this question repeatedly for each "window" and how many times they occurred
# Then it becomes a matter of accumulating how many times you came across "prefix sums you can remove" (running_sum-target) in order to get the right target. Adding this from each window for 0..I will give you the correct count

# window - each iteration in the for loop basically represents a new "window" from 0..current_index

# Gotchas
# You cannot compute the prefix sum beforehand like usual prefix sum problems. Why? Because you'd remove prefix sums outside the window you are currently dealing with. Leading to the incorrect count (over counting or duplicates).
# Implementation
# To implement this - we initialize a prefix table as a dictionary, the running sum and result counts as integers.
# Note, the dictionary must be initialized to include "0", to handle the case where the prefix sum window is exactly equal to the target. This will include the whole window in the count, as well as potentially other subarray sums that also added to 0.

# Time Complexity
# T = O(n) since we loop over each element once where n is the number of elements in the array

# Space Complexity
# S = O(n) in the worst case for storing the hashmap (on average its less than that) - all other constant variables require O(1)

# watch this vid: https://www.youtube.com/watch?v=fFVZt-6sgyo

class Solution:
    def solve(self, nums, target):
        prefixTable = {0: 1}
        prefixSum = 0
        count = 0

        for n in nums:
            prefixSum += n
            # Is there a prefix we can remove in the subarray window that will add to the target?
            # if so, add the total
            if prefixSum - target in prefixTable:
                count += prefixTable[prefixSum - target]

            if prefixSum in prefixTable:
                prefixTable[prefixSum] = prefixTable[prefixSum] + 1
            else:
                prefixTable[prefixSum] =  1

        return count
