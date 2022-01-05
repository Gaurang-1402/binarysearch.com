
# approach

# we use the quick select algorithm as the hint suggests. How to describe
# quickselect?

# first thing to do is set the low and high as the first and last index
# now in a helper function send all the useful params you have
# in this approach, we set pivot as the highest elem
# we initialize sortedElemIdx. At the end of the traversal, we will
# have this idx in the sorted spot. Everything idx lesser than sortedElemIdx
# has values lesser than value at sortedElemIdx

# we go through each idx in nums and only make a swap between i and sortedElemIdx
# if nums[i] <= pivot. NOTE we never travel to high (pivotIdx) and don't
# need to make a swap for it.

# finally we swap val at high(the pivot) with sortedElemIdx
# because we know that sortedElemIdx is in the right position

# if sortedElemIdx is less than k, we know k is on rhs - make recursive call
# if sortedElemIdx is greater than k, we know k is on lhs- make recursive call
# # if sortedElemIdx is equal to k, we can return nums[k]

# analysis

# Worst time: O(n^2) imagine you put each elem in the correct position before finding k
# where k was 0. You have a for loop foe each sorting

# worst space: O(n) imagine you put each elem in the correct position before finding k
# where k was 0. You have a recursive call n timmes so height of stackframes is n

# Average time: O(n) if arbitrarily chosen k, we converge to O(n)


class Solution:
    def solve(self, nums, k):

        low = 0
        high = len(nums) - 1

        def quickSelect(nums, k, low, high):

            sortedElemIdx, pivot = low, nums[high]
            # high is also known as pivotIdx

            for i in range(low, high):
                # last elem (pivot) is excluded in the loop
                if nums[i] <= pivot:
                    nums[sortedElemIdx], nums[i] = nums[i], nums[sortedElemIdx]
                    sortedElemIdx += 1

            nums[sortedElemIdx], nums[high] = nums[high], nums[sortedElemIdx]


            if sortedElemIdx < k:
                return quickSelect(nums, k, sortedElemIdx + 1, high)
            elif sortedElemIdx > k:
                return quickSelect(nums, k, low, sortedElemIdx - 1)
            else:
                return nums[k]

        return quickSelect(nums, k, low, high)


        
