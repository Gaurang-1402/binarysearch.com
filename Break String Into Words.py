
# approach

# we first draw the decision tree for this problem
# the only way that we can return true based on the decision tree
# is if we pass s as an empty string which becomes our base case

# we traverse through each slice available in s using indices and
# try to match it with a word

# we use backtracking here. the constraint is if the word in words
# matches the slice of the words we made, then we can recurse further

# we return false if we went through entire s and found no slice matches

# analysis
# m is len of s n is len of words
# T(n) = O(m^2*n)
# S(n) = O(m)


class Solution:
    def solve(self, words, s):

        # edge cases
        if s == '':
            return True


        def wordSolver(words, s, memo):

            if s in memo:
                return memo[s]

            # we only return true if we reach the empty string
            if s == '':
                return True

            for i in range(len(s)): # m

                for word in words:
                    if s[0: i + 1] == word:
                        newWord = s[i+1:]
                        if wordSolver(words, newWord, memo) == True:
                            memo[s] = True
                            return memo[s]
            memo[s] = False
            return memo[s]


        return wordSolver(words, s, {})
        
