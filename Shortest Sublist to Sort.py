class Solution:

     # https://leetcode.com/problems/shortest-unsorted-continuous-subarray/discuss/1573889/Easy-to-understand-solution-Time-O(n)-Space-O(1)-Python-Iterative


    def solve(self, nums):

        # error checks

        if (len(nums) == 0):
            return 0

        if (len(nums) == 1):
            return 0


        minUnsortedVal = float("inf")
        maxUnsortedVal = float("-inf")

        for i in range(len(nums)):
            current = nums[i]
            if self.isOutOfOrder(nums, current, i):
                maxUnsortedVal = max(current, maxUnsortedVal)
                minUnsortedVal = min(current, minUnsortedVal)


        if minUnsortedVal == float("inf") and maxUnsortedVal == float("-inf"):
            return 0


        left = 0

        right = len(nums) - 1

        while nums[left] <= minUnsortedVal:
            left += 1

        while nums[right] >= maxUnsortedVal:
            right -= 1

        return right - left + 1


    def isOutOfOrder(self, nums, current, i):

        if i == 0:
            return nums[i] > nums[i + 1]

        if i == len(nums) - 1:
            return nums[i-1] > nums[i]

        return nums[i] > nums[i + 1] or nums[i-1] > nums[i]


        # maxUnsortedLen = 0
        # while left <= right:
        #     if nums[left] <= nums[right]:
        #         left += 1
        #         right -= 1

        #     else:
        #         maxUnsortedLen = right - left + 1
        #         return maxUnsortedLen


        # return maxUnsortedLen


        # # bruteforce

        # i = 0



        # while i < len(nums) - 1:

        #     if nums[i] <= nums[i + 1]:
        #         i += 1
        #         continue
        #     else:
        #         unsortedLen = 1
        #         while i < len(nums) - 1 and nums[i] > nums[i + 1]:
        #             unsortedLen += 1
        #             i += 1

        #         maxUnsortedLen = max(unsortedLen, maxUnsortedLen)


        # return maxUnsortedLen


        
