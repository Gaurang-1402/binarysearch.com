# approach

# impoertant thing to note is that we have a square.

# we can add our markers sR, eR, sC, eC at the appropriate indices
# we will update these markers after each row has been transformed

# since the matrix is a square, we need to do the rotations eR - sR
# times (len of the row/column) this gets dynamically updted as we
# move to inner values and need to shrink number of times we perform operations

# instead of starting the shift with topLeft, we start by changing topLeft
# before we shift we save it. Now we only need to save one var that will update
# the last value to change in our matrix

# read the comments now

# analysis

# T = O(n * n) since n is a square
# S = O(k) no extra space being used

class Solution:
    def solve(self, matrix):

        sR = 0
        eR = len(matrix) - 1

        sC = 0
        eC = len(matrix[0]) - 1

        while sR <= eR and sC <= eC:
            
            # how many times do we need to shift
            # if sR = 0 and eR = 3 then we need to shift 3 times
            # 3 - 0 = 3
            for i in range(eR - sR):
                # save top left
                topLeft = matrix[sR][sC + i]

                # top right to top left
                matrix[sR][sC + i] = matrix[sR + i][eC]

                # bottom right to top right
                matrix[sR + i][eC] = matrix[eR][eC - i]

                # bottom left to bottom right
                matrix[eR][eC - i] = matrix[eR - i][sC]

                # top left to bottom left
                matrix[eR - i][sC] = topLeft

            sR += 1
            eR -= 1
            sC += 1
            eC -= 1

        return matrix




        
