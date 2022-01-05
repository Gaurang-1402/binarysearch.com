class Solution:
    def solve(self, s):

        def recursiveSolveHelper(s, low, high):
            if low >= high:
                return True

            return s[low] == s[high] and recursiveSolveHelper(s, low+1, high-1)

        return recursiveSolveHelper(s, 0, len(s) - 1)


        # low = 0
        # high = len(s) - 1

        # while high > low:
        #     if s[high] != s[low]:
        #         return False

        #     high -= 1
        #     low += 1

        # return True






        
