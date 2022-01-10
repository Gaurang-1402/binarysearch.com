# approach
# maintain four pointers- maxNum, secondMaxNum, minNum and secondMinNum
# update maxNum if num is bigger and also update secondMaxNum simultaneously

# the special case is that we update secondMaxNum also if num >= secondMaxNum but
# smaller than maxNum

# same idea for minNums as well

# finally return the max of products of maxNums and products of minNums

# analysis
# we go through each num once so time taken is
# T = O(n) where n is number of nums

# we only store fours pointers so space complexity is
# S = O(n)

class Solution:
    def solve(self, nums):

        maxNum = float("-inf")
        secondMaxNum = float("-inf")

        minNum = float("inf")
        secondMinNum = float("inf")

        for num in nums:
            if num >= maxNum:
                secondMaxNum = maxNum
                maxNum = num
            elif num >= secondMaxNum:
                secondMaxNum = num

            if num <= minNum:
                secondMinNum = minNum
                minNum = num
            elif num <= secondMinNum:
                secondMinNum = num

        return max(maxNum * secondMaxNum, minNum * secondMinNum)
