# approach
# first collect all the unique values vals
# and a frequency: how many times they occur fre
# Now that we have these two, keep trying to make a list of k consecutive elements starting from the smallest value in vals

# Implementation
# put all the unique values in a min heap

# now for making a list of k elements, just pop the min start

# check if all the values in [start, start+1,start+2....start+k) exist in nums

# any point i find a element that doesn't exist i return false, since we cannot make a consecutive list ;)

# at the end since we have used some elements and REDUCED their remaining frequency => we will delete those elements from the heap which have a fre == 0 :D

# analysis
# Time Complexity
# T = O(nlogn) since each element is popped from the stack atmost once; why not O(K * N Log N)?
# Because amortized, there are only N//K values of start so the for loop will run for a total of N//k * k = N ;)

# Space Complexity
# S = O(n) for the fre Counter and the vals heapq

class Solution:
    def solve(self, nums, k):
        count = Counter(nums)
        roots = [x for x in nums if x - 1 not in count]

        while roots:
            r = roots.pop()
            # if a potential root was used up, continue to next root
            if count[r] <= 0:
                continue
            # use up the next k consecutive numbers
            for i in range(r, r + k):
                if not count[i]:
                    return False
                count[i] -= 1
                # Add any new roots we find
                if count[i] and not count[i - 1]:
                    roots.append(i)

            # check if next number after the sequence is a potential root
            if count[r + k] and not count[r + k - 1]:
                roots.append(r + k)

        return True

