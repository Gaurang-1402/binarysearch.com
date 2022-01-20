# approach
# watch this explanation: https://www.youtube.com/watch?v=ayAtHIwU3Zw
# it is important to understand that both the val and indices of nums matter

# convert n to list for easy swapping
# we first create a dict that maps the val of a num in n to its idx (if we have
# duplicate nums, we overwrite the idx to be the higher one of the duplicates)

# for each num in n, we see if there is a larger potentialNum available from 9 to num, and if it is
# if the index of potentialNum is greater than idx of num (which means potentialNum is behind num in numChars)

# we make the swap using the indices we have and return

# analysis
# n is the length of n

# time complexity is
# T = O(n) because the inner for loop is only being run at most 9 times which is a constant and
# the joining and list creation happens only once because we return in the if condition so it gets added instead of
# being multiplied.

# space complexity is
# S = O(n) because you save n in a hash map and list

class Solution:
    def solve(self, n):

        numChars = [int(val) for val in str(n)]
        numDict = {val:idx for idx, val in enumerate(numChars)}

        for i, num in enumerate(numChars):
            for potentialNum in range(9, num, -1):
                if potentialNum in numDict and numDict[potentialNum] > i:
                    numChars[i], numChars[numDict[potentialNum]] = numChars[numDict[potentialNum]], numChars[i]
                    return int("".join([str(char) for char in numChars]))

        return int("".join([str(char) for char in numChars]))
