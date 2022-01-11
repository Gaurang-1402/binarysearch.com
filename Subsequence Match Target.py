# approach
# the explanation for this approach: https://www.youtube.com/watch?v=Vch3pFgmKD8

# analysis
# worst case --> Imagine s="aaaa..." and words=["aaa..." , "aaaa..." , "aaaa...", ...]
# time complexity is
# T = O(n * m) where n is the length of the s and m is the length of the words

# space complexity is
# S = O(m) where m is the length of the words


class Solution:
    def solve(self, words, s):

        mapFirstCharToWord = defaultdict(list)
        # save all words grouped by their starting characters in a dict
        for word in words:
            mapFirstCharToWord[word[0]].append(word)

        result = 0
        # go by each character in c
        for char in s:
            # get all words in dict that start with the character c
            allWordsBeginningWithChar = mapFirstCharToWord[char]

            # clear the existing list
            mapFirstCharToWord[char] = []

            # go through all the words in the list that start with c
            for word in allWordsBeginningWithChar:
                # check  for the ones that only have 1 char left. that means that
                # this word was completed and we can increment the ans variable
                if len(word) == 1:
                    result += 1

                else:
                    # else, there are still characters left in this word so we can just add the remaining word to the list for the 2nd character in the list
                    mapFirstCharToWord[word[1]].append(word[1:])


        return result


        #A brute force thinking - Generate all the subsequences of s and store them in an array
        #find how many of them occurs in the given array "words", count them and return them
        #But as we know, for a string of length n, we will have 2^n subsequences,
        #so the Time Complexity will definitely throw TLE


        #Lets try to think another way now


        #We can try to map the concept used in the problem Is Subsequence (Problem 392) here
		#Checking it out before this problem can be really useful as in this problem, we were given two separate strings
		#and we were supposed to check if one is a subsequence of other or not

        #Below Approach clears 41 / 52 test cases and then throws TLE

        # count = 0
        # for k in words:
        #     i = 0 #to keep a check across k where k is an element of given array "words"
        #     j = 0 #to keep a check across s

        #     while j < len(s) and i < len(k):

        #         if k[i] == s[j]: #if words are similar, move through both the strings
        #             i += 1
        #             j += 1
        #         else: #if they are not, just move through characters of s
        #             j += 1

        #     if i == len(k): #if i covers all elements of k, it means it is a subsequence
        #         count += 1

        # return count
