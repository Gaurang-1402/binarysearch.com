# intuition
# this is a intervals question so it helps to draw out a number line to see what is happening.
# sorting the intervals would help because we can arrange the number lines in a sorted manner.
# if the start of any given interval i is greater or equal to the end of interval i-1 then no removal neccesary.
# otherwise there is a overlap and between i and i-1 the interval with a longer end should be removed (because
# longer interval may have a larger chance of overlapping with a future interval)

# implementation
# we sort the intervals first thing, check edge case if len(intervals) == 0. The approach is greedy because of sorting
# in line comments explain the approach

# analysis
# time taken to sort n elems is
# T = O(nlogn)

# space occupied is
# S = O(k)

# resources
# https://www.youtube.com/watch?v=nONCGxWoUfM

class Solution:
    def solve(self, intervals):

        if len(intervals) == 0:
            return 0

        # sort the intervals according to the first val in the interval
        intervals.sort()
        prevEnd = intervals[0][1]

        removalCount = 0

        for start, end in intervals[1:]: # first interval is picked before so go from first idx
            if start >= prevEnd:
                prevEnd = end
            else:
                removalCount += 1
                prevEnd = min(end, prevEnd) # we want the shorter end for comparison, longer one is "removed" because it has a greater chance of overlapping

        return removalCount


