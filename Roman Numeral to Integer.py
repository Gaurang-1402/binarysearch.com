# approach

# First we create a conversion dictionary. We need to deal
# IV = -1 + 5
# VI = 5 + 1
# XL = -10 + 50
# LX = 50 + 10
# So, if a smaller number appears before a larger number, it indicates that the number
# is smaller by a quantity used as a suffix to it, which made going backwards seem easy.

# analysis

# since we go through each index in the string, if the string has n numbers, the time complexity is
# T = O(n)

# since we store a constant size of conversion in a dictionary, the space complexity is
# S = O(k)


class Solution:
    def solve(self, numeral):

        romanNumbersToReal = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        res, tmp = 0, 0

        for i in reversed(numeral):

            if romanNumbersToReal[i] >= tmp:
                res = res + romanNumbersToReal[i]
            else:
                res = res - romanNumbersToReal[i]
            tmp = romanNumbersToReal[i]

        return res



