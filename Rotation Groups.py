# approach
# maintain a combinationSet
# each time you come across a word, check if that word is
# present in combinationsSet.

# if it is not the count can be incremented. we also want to ensure
# that all possible rotations of that word are added to the combinationsSet
# which we do with a seperate for loop

# it is very interesting to see how you generate rotations in a string done like this

# for j in range(len(word)):
#     combinationsSet.add( word[j:] + word[:j]   )

# this gets the rotating ending part + rotating starting part

# analysis
# Time Complexity
# T = O(n^2) all the rotations of all the words might be checked in the worst case

# Space Complexity
# S = O(n), just one representative for each group is stored. In the worst case, we store all the words.

class Solution:
    def solve(self, words):

        # bruteforce approach

        combinationsSet = set()
        count = 0

        for word in words:
            if word not in combinationsSet:
                count += 1
            for j in range(len(word)):
                combinationsSet.add(word[j:] + word[:j])

        return count


