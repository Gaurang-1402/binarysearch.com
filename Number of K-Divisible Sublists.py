# approach
# watch this to understand: https://www.youtube.com/watch?v=p2UDld3rM_Q
# this problem uses the prefix sum technique (shown by the runningSum variable)

# we create a map that maps the modulos to the number of times we have come across those modulos
# the main idea is to understand what elems we can remove

# if we encounter a modulo for the first time, we save it in the dict and set the count as 1
# if the modulo has been encountered before, we increment the result with the count of the modulos before

# the seed value of starting { 0:1 }, we ensure that when k divides, we increment result by the count

# analysis
# we go through each elem in nums so if there are n elems, time complexity is
# T = O(n)

# we save at most k elems (think about the remainder theorem from discrete) so space complexity is
# S = O(k)

class Solution:
    def solve(self, nums, k):

        result = 0
        runningSum = 0
        moduloToCountMap = { 0:1 } # maps modulo to count of us getting that modulo

        for num in nums:
            runningSum += num
            modulo = runningSum % k

            if modulo in moduloToCountMap:
                result += moduloToCountMap[modulo]
                moduloToCountMap[modulo] += 1
            else:
                moduloToCountMap[modulo] = 1


        return result



        
