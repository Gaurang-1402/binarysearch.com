
class Solution:
    def solve(self, matrix, k):
        if not matrix or not matrix[0]:
            return matrix
        n, m = len(matrix), len(matrix[0])
        pre = [[0 for j in range(m + 1)] for i in range(n + 1)]
        for i in range(n):
            for j in range(m):
                pre[i + 1][j + 1] = matrix[i][j] + pre[i][j + 1] + pre[i + 1][j] - pre[i][j]
        res = [[0 for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                a, b, c, d = max(0, i - k), max(0, j - k), min(n, i + k + 1), min(m, j + k + 1)
                res[i][j] = pre[c][d] - pre[a][d] - pre[c][b] + pre[a][b]
        return res

# my solution
# class Solution:
#     def solve(self, matrix, k):

#         sumMatrix = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]

#         for i in range(len(matrix)):
#             row = matrix[i]
#             for j in range(len(row)):

#                 rowIndexUp = i
#                 while rowIndexUp > 0 and rowIndexUp != i - k:
#                     rowIndexUp -= 1


#                 rowIndexDown = i
#                 while rowIndexDown < len(matrix)-1 and rowIndexDown != i + k:
#                     rowIndexDown += 1


#                 colIndexLeft = j
#                 while colIndexLeft > 0 and colIndexLeft != j - k:
#                     colIndexLeft -= 1


#                 colIndexRight = j
#                 while colIndexRight <= len(matrix[i]) - 1 and colIndexRight != j + k:
#                     colIndexRight += 1

#                 for rowInRange in range(rowIndexUp, rowIndexDown+1):
#                     sumMatrix[i][j] += sum(matrix[rowInRange][colIndexLeft : colIndexRight+1])

#         return sumMatrix







