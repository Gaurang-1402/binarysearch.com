class Solution:
    def solve(self, matrix):

        # O(n*m) | O(n*m)

        # edge cases

        if matrix == []:
            return []


        # initialize

        startRow = 0
        endRow = len(matrix) - 1
        startCol = 0
        endCol = len(matrix[0]) - 1

        result = []

        while startRow <= endRow and startCol <= endCol:

            for c in range(startCol, endCol+1):
                result.append(matrix[startRow][c])

            for r in range(startRow+1, endRow + 1):
                result.append(matrix[r][endCol])

            for c in reversed(range(startCol, endCol)):
                if startRow == endRow:
                    break
                result.append(matrix[endRow][c])

            for r in reversed(range(startRow+1, endRow)):
                if startCol == endCol:
                    break
                result.append(matrix[r][startCol])

            startRow += 1
            endRow -= 1
            startCol += 1
            endCol -= 1


        return result
        
