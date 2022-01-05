class Solution:
    def solve(self, nums):

        # edge cases

        if len(nums) == 0:
            return -1

        if len(nums) == 1:
            return 0

        if len(nums) == 2:
            return 2

        # main


        dp = {}

        dp[1] = (nums[1] - nums[0], 2, 0)

        result = 0

        for i in range(2, len(nums)):
            currDiff = nums[i] - nums[i-1]
            prevDiff, prevLen, prevCount = dp[i - 1]

            if prevDiff == currDiff:
                dp[i] = (currDiff, prevLen+1, prevCount+1)

            else:
                dp[i] = (currDiff, 2, 0)

            result += dp[i][2]

        return result




        # bruteforce

        # seqCount = 0

        # for i in range(len(nums) - 1):
        #     currIdx = i
        #     currElem = nums[i]

        #     diff = nums[i + 1] - nums[i]

        #     while currIdx < len(nums) - 1 and (nums[currIdx + 1]  - nums[currIdx] == diff):
        #         if currIdx - i + 1 >= 2:
        #             seqCount += 1
        #         currIdx += 1


        # return seqCount
        
