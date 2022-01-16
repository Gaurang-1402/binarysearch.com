# approach
# classic heap problem, watch this: https://www.youtube.com/watch?v=itmhHWaHupI
# maintain two heaps- small and large. The small is a maxHeap and large is a minHeap.
# Why is small a maxHeap?
# we want to order this class such that the middle two values are in the sorted order. So small
# is the first half of the class with the maximum value at the top
# Why is large a maxHeap?
# we want to order this class such that the middle two values are in the sorted order. So large
# is the second half of the class with the minimum value at the top - O(k) access

# in the add method, we append to small each time the method is called. If the maximum in small is greater than
# minimum in large, we remove the max in small and add it to large.

# if the differnce in elems in small and large is more than 1 and small is bigger, we transfer small's max
# to large's min

# if the differnce in elems in small and large is more than 1 and large is bigger, we transfer large's min
# to small's max

# for median method, special case when small, large are same size, we return the average of the tops
# otherwise the larger one's min or max is returned

# analysis
# each heappush and heappop costs logn time. So worst time taken in method add is
# T = O(logn)

# we hold n numbers in the class so space complexity is
# S = O(n)

class RollingMedian:
    def __init__(self):
        # maintain max heap in small
        self.small = []

        # maintain min heap in large
        self.large = []


    # T = O(logn)
    def add(self, val):
        heapq.heappush(self.small, -1 * val)

        # val in small max is greater than val in large min
        if (self.small and self.large and -1 * self.small[0] > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # uneven number of elems
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)
    # T = O(k)
    def median(self):
        if len(self.small) == len(self.large):
            return ((-1 * self.small[0] + self.large[0]) / 2)
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.small) < len(self.large):
            return self.large[0]
                
