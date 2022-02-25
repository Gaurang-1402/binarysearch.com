# intuition
# A property of a palindrome is that it can have at most one unique character that occurs odd number of times.
# we just need to see if oddCount <= 1 in a string

# implementation
# maintain a charCount dict with the count of each char in the string
# go through the charCounts.values() and if the val is odd count it
# return true only if oddNum <= 1

# analysis
# we go through each elem in a string of length n so the time complexity is
# T = O(n)

# we save the count and char in the dictionary
# S = O(n)

class Solution:
    def solve(self, s):
        charCount = Counter(s) # maps char -> charCount
        oddNum = 0
        for val in charCount.values():
            if val % 2:
                oddNum += 1

        return oddNum <= 1

