# approach
# watch this: https://www.youtube.com/watch?v=Akt3glAwyfY&t=874s
# we use the line sweep technique- used in intervals
# we start by sorting the starting points and ending points of the intervals in two seperate lists

# we maintain two pointers one on starting list and other on ending list
# if we find that start is lesser, we increment counter meaning we need a movie theater occupied
# if we find that end is lesser, we decrement counter meaning a theater is freed

# we keep track of the largest count throughout

# analysis
# we sort the lists and with the best case sorting algorithm,
# T = O(nlog(n))

# we don't use any extra space so space complexity is
# S = O(k)

class Solution:
    def solve(self, intervals):
        starts = sorted([interval[0] for interval in intervals])
        ends = sorted([interval[1] for interval in intervals])

        startP = 0
        endP = 0

        maxCount = 0
        currCount = 0

        while startP < len(starts) and endP < len(ends):

            currStart = starts[startP]
            currEnd = ends[endP]

            if currStart < currEnd:
                currCount += 1
                startP += 1
            else:
                currCount -= 1
                endP += 1

            maxCount = max(maxCount, currCount)

        return maxCount



