# approach
# sort the numbers
# now you can pick each elem, and then find the next 2 elems (from the front and back) that when combined, all sum up to k
# depending on how big the sum of 3 elems is, you increment or decrement low or high.
# if you find the sum, return True

# analysis
# the sorting costs nlogn but the two loops make it so that the time complexity is
# T = O(n^2)

# no extra space used so time complexity is
# S = O(k)

class Solution:
    def solve(self, nums, k):
        nums.sort()
        for i in range(len(nums) - 2):
            low = i + 1
            high = len(nums) - 1
            currNum = nums[i]

            while high > low:
                highNum = nums[high]
                lowNum = nums[low]
                if (currNum + highNum + lowNum) == k:
                    return True
                elif (currNum + highNum + lowNum) < k:
                    low += 1
                elif (currNum + highNum + lowNum) > k:
                    high -= 1

        return False

