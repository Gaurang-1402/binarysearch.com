# approach
# we maintain two pointers one on source and the other on target
# sourceP is always initialized to 0
# we find the first common letter in source and target. We keep incrementing targetP and sourceP so long as
# source and target strings are the same
# in case they are not, only sourceP gets icremented

# note that there is no concatenation or anything. We only go through source and try to find the best match
# of subsequence

# analysis

# since we iterate through source, with m elems, and target, with n elems, the time complexity is
# T = O(n * m)

# we only save extra pointers so space complexity is
# S = O(k)


class Solution:
    def solve(self, source, target):

        sourceP = 0
        targetP = 0

        numberOfSubSequences = 0

        while targetP < len(target):

            sourceP = 0

            while sourceP < len(source) and source[sourceP] != target[targetP]:
                sourceP += 1

            if sourceP == len(source):
                return -1
            while sourceP < len(source) and targetP < len(target):

                if source[sourceP] == target[targetP]:
                    sourceP += 1
                    targetP += 1
                else:
                    sourceP += 1

            numberOfSubSequences += 1


        return numberOfSubSequences




