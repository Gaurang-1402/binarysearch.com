class Solution:
    def solve(self, nums):

        minIdxNum = float("inf")

        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == mid:
                print(mid)
                minIdxNum = min(mid, minIdxNum)
                low -=1
                high -= 1


            elif nums[mid] > mid:

                high = mid - 1


            else:

                low = mid + 1

        return -1 if minIdxNum == float("inf") else minIdxNum

        
