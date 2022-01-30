# approach
# go through each index in the string and consider it the middle of a palinfrome

# now consider 2 cases:
# for index i,
# imagine the palindrome length is odd and compare i + 1 and i - 1
# keep going left and right simultaneously and seeing if the palindrome maintains

# for index i,
# imagine the palindrome length is even and i and i - 1
# keep going left and right simultaneously and seeing if the palindrome maintains

# analysis
# since for each index we possibly traverse through the whole string
# T = O(n)
# since no other data structure is used to store,
# S = O(k)

class Solution:
    def solve(self, s):

        numOfPalinDromes = len(s)

        right = 0
        left = 0

        for i in range(len(s)):

            # imagine the palindrome length is odd and compare +1 and -1
            right = i + 1
            left = i - 1
            while right < len(s) and left >= 0 and s[left] == s[right]:
                numOfPalinDromes += 1
                left -= 1
                right += 1

            # imagine the palindrome length is even and compare one backwards
            right = i
            left = i - 1
            while right < len(s) and left >= 0 and s[left] == s[right]:
                numOfPalinDromes += 1
                left -= 1
                right += 1

            # finally increment i
            i += 1

        return numOfPalinDromes
