class Solution:
    def solve(self, nums):

        negativeMap = {}

        for num in nums:
            if num <= 0:
                negativeMap[-num] = num


        maxNum = -1
        for num in nums:
            if num > 0 and num in negativeMap:
                maxNum = max(num, maxNum)

        return 0 if 0 in negativeMap and maxNum == -1 else maxNum




        
