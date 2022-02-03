# approach
# we can maintain a leftMultiplications starting from left (for the first index take the val 1) and a
# rightMultiplications list which goes from right to left (for the first index take the val 1)

# now we need to multiply leftMultiplications[i] and rightMultiplications[i] to get the ans at any index i

# analysis
# we go through the list multiple times
# T = O(n)

# we save a new list so space complexity is
# S = O(n)

class Solution:
    def solve(self, nums):

        leftMultiplications = [1]
        rightMultiplications = [1]

        leftPointer = 1
        while leftPointer < len(nums):
            leftMultiplications.append(nums[leftPointer - 1] * leftMultiplications[-1])
            leftPointer += 1

        nums.reverse()

        rightPointer = 1
        while rightPointer < len(nums):
            rightMultiplications.append(nums[rightPointer - 1] * rightMultiplications[-1])
            rightPointer += 1

        nums.reverse()
        rightMultiplications.reverse()
        return [rightMultiplications[i] * leftMultiplications[i] for i in range(len(nums))]
