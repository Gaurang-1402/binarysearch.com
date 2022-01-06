# approach

# it is useful to use the greedy method here. But before we use the greedy method, we need to enable
# optimal substructure.

# this can be done by sorting by the first elem of the intervals see how we do it

# now that we know that the intervals are sorted according to the beginning of those intervals
# the method is to add the first elem of the sorted intervals in the merged intervals.

# now the key is to compare each elem from index 1 to end of matrix with the already merged list at the top of the mergedIntervals
# there are three cases

# end of curr is less than end or prev --> skip doing anything
# start of curr is less than equal to end of prev --> update end of prev with curr end
# neither of these --> add curr as a new interval

# analysis
# the most expensive operation in terms of time is sorting. The time complexity for this is
# T = O(nlogn) where n is number of lists in matrix

# the space complexity as a result of creating a new mergedInterval is
# S = O(n) imagine worst case scenario no overlaps between any list


class Solution:
    def solve(self, intervals):
        # edge case
        if len(intervals) == 0:
            return [[]]

        sortedIntervals = sorted(intervals, key = lambda x:x[0])
        mergedIntervals = [sortedIntervals[0]]

        for i in range(1, len(sortedIntervals)):
            interval = sortedIntervals[i]
            currStart, currEnd = interval

            prevStart, prevEnd = mergedIntervals[-1]

            if currEnd <= prevEnd:
                continue
            elif currStart <= prevEnd:
                mergedIntervals[-1][1] = currEnd
            else:
                mergedIntervals.append(sortedIntervals[i])

        return mergedIntervals



        
