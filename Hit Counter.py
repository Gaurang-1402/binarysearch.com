# approach
# I am given timestamps in increasing order...
# Also, we are only interested in timestamps that occur in a 60 second window

# maintain invariant ⬇️
# "window only contains latest 60 seconds"
# Normal sliding window ;)

# add to the right side of the window

# pop from the left side we want to remove the earliest values (FIFOs)

# Implementation
# who to pop?
# we want only 60 seconds in this window....
# So I want to pop all values that come before timestamp - 60 ;)
# ^^ popAllBefore() ^^

# Let's use a queue?

# add from back

# while front timestamp is too old ( - 60 ):
#     pop from left
# And when I want to count()

# I just do this -> return len(q) ;)


# analysis
# Time Complexity
# T = O(n) worst case for either BUT over n calls, O(1) amortized ( I am calling popAllBefore() inside both functions and any element is always pushed and popped from the queue at most once )

# Space Complexity
# S = O(n) because it might happen that all the n elements added are in the same second ( or same 60 second window ;)

class HitCounter:
    def __init__(self):
        self.q = deque()

    def add(self, timestamp):
        self.popAllBefore(timestamp - 60)
        self.q.append(timestamp)

    def count(self, timestamp):
        self.popAllBefore(timestamp - 60)
        return len(self.q)

    def popAllBefore(self, timestamp):
        while self.q and self.q[0] < timestamp:
            self.q.popleft()

