class Solution:
    def solve(self, s0, s1):


        # Get dimensions
        n = len(s0)
        m = len(s1)

        # Ensure n < m
        if m < n:
            return self.solve(s1, s0)

        # Check if length diff is > 1
        if abs(n - m) > 1:
            return False

        # index i -> s0, index j -> s1
        i = 0
        j = 0
        edits = 0
        while i < n:
            # chars match, increment i, j :D
            if s0[i] == s1[j]:
                i += 1
                j += 1
            # mismatch, count edit >:(
            else:
                edits += 1

                # same length, replace char in s0, move i, j
                if n == m:
                    i += 1
                    j += 1
                # not same length, delete char from s1 by moving j
                else:
                    j += 1

            # too many edits, terminate
            if edits > 1:
                break

        # 1 edit or less?
        return edits <= 1


        # base string will always be s0 and string being checked is s1


        # def checkForAddition(s0, s1):
        #     # check what can be added from s0 into s1
        #     addCount = 0

        #     p0 = p1 = 0

        #     while p0 < len(s0):
        #         if p1 >= len(s0):
        #             return False

        #         if p0 >= len(s1):
        #             addCount += 1
        #             p0 += 1
        #             p1 += 1
        #             continue
        #         if s0[p0] != s1[p0]:
        #             addCount += 1


        #         else:
        #             p0 += 1
        #             p1 += 1


        #     return addCount == 1

        # def checkForDeletion(s0, s1):
        #     # check what can be deleted from s1 into s0
        #     deleteCount = 0

        #     for p1 in range(len(s1)):

        #         if p1 >= len(s0):
        #             deleteCount += 1
        #             continue
        #         elif s0[p1] != s1[p1]:
        #             deleteCount += 1

        #     return deleteCount == 1

        # def checkForReplacement(s0, s1):
        #     # check what can be replaced from s0 into s1
        #     replaceCount = 0

        #     for p1 in range(len(s1)):
        #         if s0[p1] != s1[p1]:
        #             replaceCount += 1

        #     return replaceCount == 1


        # if s0 == s1:
        #     return True

        # if len(s0) - len(s1) == 1:
        #     return checkForAddition(s0, s1)

        # elif len(s0) - len(s1) == -1:
        #     return checkForDeletion(s0, s1)

        # elif len(s0) - len(s1) == 0:
        #     return checkForReplacement(s0, s1)

        # else:
        #     return False

        
