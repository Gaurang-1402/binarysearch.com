# approach
# don't complicate this question by thinking about it like a graph.
# Keep it simple by going through each row and each column

# for the row check, use Python overpowered functionality to turn a list into a word
# using join method. You can then use the "in" keyword to see if the chars in word
# are present in the entire row joined

# for col check, first make the word in the column itself (we are doing col by col traversal over row by row traversal)/
# You can then use the "in" keyword to see if the chars in word are present in the entire col joined

# otherwise return false

# analysis
# r is the number of rows, c is the number of cols and m is the number of chars in word
# T = O(r * c) or O(r**2) or O(r * m) depending on the input

# space we use is mainly for storing the word with m characters
# S = O(m)

class Solution:
    def solve(self, board, word):

        ROWS = len(board)
        COLS = len(board[0])

        for row in board:
            potentialWord = "".join(row)

            if word in potentialWord:
                return True

        # note that we are going through each column first
        for col in range(COLS):
            potentialWord = ""
            # and then going through each row
            for row in range(ROWS):
                potentialWord += board[row][col]

            if word in potentialWord:
                return True

        return False


        # ==================================

        # Graph way

        # ROWS = len(board)
        # COLS = len(board[0])


        # def exploreRight(r, c, idx):
        #     if idx == len(word):
        #         return True
        #     if r >= len(board) or c >= len(board[0]):
        #         return False
        #     if board[r][c] == word[idx]:
        #         return exploreRight(r, c + 1, idx + 1)
        #     else:
        #         return False


        # def exploreDown(r, c, idx):
        #     if idx == len(word):
        #         return True
        #     if r >= len(board) or c >= len(board[0]):
        #         return False
        #     if board[r][c] == word[idx]:
        #         return exploreDown(r + 1, c, idx + 1)
        #     else:
        #         return False


        # for row in range(ROWS):
        #     for col in range(COLS):
        #         if board[row][col] == word[0]:
        #             if exploreRight(row, col+1, 1) or exploreDown(row+1, col, 1):
        #                 return True

        # return False
