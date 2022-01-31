# approach
# important thing to remember is that a dictionary cannot be used as a key
# but we can make a string a key.

# now how do we make all the anagrams the same?
# idea is to sort the string.
# now after it has been sorted we can make it the key
# and the val is the count of the sorted anagram.

# we keep incrementing the count as we find same anagrams
# finally return the maximum count of the anagram

# analysis
# first lets define the lengths
# length of words --> n
# length of the longest word --> m

# worst case time, we sort the longest word and get
# T = O(n * m * log(m))

# worst case we save each word in the dict so space is
# S = O(n) or O(n * m) if you consider smallest unit a character

class Solution:
    def solve(self, words):

        hashMap = {} # {anagramSorted: count}
        for anag in words:
            # sorted function = convertStringToList --> sort
            key = "".join(sorted(anag)) # we have to convertListToString afterwards

            # sorted anagram being used as a key
            if key in hashMap.keys():
                hashMap[key] += 1
            else:
                hashMap[key] = 1

        return max([count for key, count in hashMap.items()])

        # brute force approach

        # lstOfDict = []

        # for word in words:
        #     wordDict = Counter(word)

        #     doesNotExist = True

        #     for i in range(len(lstOfDict)):
        #         prevDict, count = lstOfDict[i]
        #         if wordDict == prevDict:
        #             lstOfDict[i][1] += 1
        #             doesNotExist = False
        #             break

        #     if doesNotExist:
        #         lstOfDict.append([wordDict, 1])

        # return max([count for prevDict, count in lstOfDict])
