from collections import deque
class Solution:
    def solve(self, nums, k):


        minQueue = deque()
        maxQueue = deque()

        maxRes = 0
        start = 0

        for end in range(len(nums)):
            curr =  nums[end]
            while len(maxQueue) and nums[maxQueue[-1]] < curr:
                maxQueue.pop()

            maxQueue.append(end)

            while len(minQueue) and nums[minQueue[-1]] > curr:
                minQueue.pop()

            minQueue.append(end)

            maxElem = nums[maxQueue[0]]
            minElem = nums[minQueue[0]]

            if (abs(maxElem - minElem) <= k):
                maxRes = max(maxRes, end - start + 1)

            else:

                # shrink window
                if start == maxQueue[0]:
                    maxQueue.popleft()
                if start == minQueue[0]:
                    minQueue.popleft()

                start += 1

        return maxRes


