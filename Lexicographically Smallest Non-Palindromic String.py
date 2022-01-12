# approach
# The smallest lexographic character is 'a'
# For obtaining the lexicographically smallest sequence by replacing a single character we must change the earliest
# (from left to right) valid character to 'a'.
# When iterating from left --> right. The first character which is not 'a' must be replaced by 'a'.
# In a palindromic sequence, we observe the same set of characters in the first half as the second half.

# in a case where all characters are 'a's, the previous algorithm won't work
# to handle this case, we find the first 'a' from the back and change it to a 'b'

# analysis
# since we go through each char in n chars, time complexity is
# T = O(n)

# we save string as a list so space complexity is
# S = O(n)

class Solution:
    def solve(self, s):

        # edge case
        if len(s) == 1:
            return s

        # convert to list
        palindromeList = list(s)

        for i in range(len(palindromeList)):
            if palindromeList[i] != "a":
                palindromeList[i] = "a"
                break

        if palindromeList != palindromeList[::-1]:
            return "".join(palindromeList)

        # if we get here, it means that all characters are 'a's

        palindromeList = list(s)
        for i in range(len(palindromeList)-1,-1,-1):
            if palindromeList[i] == "a":
                palindromeList[i] = "b"
                break

        return "".join(palindromeList)

