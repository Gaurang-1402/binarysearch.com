
from collections import deque
from collections import defaultdict
# watch this: https://www.youtube.com/watch?v=s8p8ukTyA2I

# intuition
# we can notice that for each choice, we need to use the most
# frequent character at that moment
# maxHeap should be a good choice to keep track of the most frequent elem


# implementation
# first count all the occurrences of each integer
# create a maxHeap by heapifying with the count of integers
# the queue maintains the count and the time at which the count can be added back

# analysis
# go through each elem where length is n and m is the length of the queue
# T = O(n + m)

# the queue and heap takes space so space is
# S = O(n + m)

class Solution:
    def solve(self, nums, k):

        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1

        maxHeap = [-count for count in counter.values()] # stores [-count, ...] to become a maxHeap
        heapq.heapify(maxHeap)

        timePassed = 0

        queue = deque() # stores [countOfElem, timeAfterWhichEligibleToAddToMaxHeap]

        while len(maxHeap) or len(queue):
            timePassed += 1

            if len(maxHeap):
                newCount = 1 + heapq.heappop(maxHeap)
                if newCount:
                    queue.append([newCount, timePassed + k])

            if len(queue) and timePassed == queue[0][1]:
                heapq.heappush(maxHeap, queue.popleft()[0]) # runs O(logn)

        return timePassed
