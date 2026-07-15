class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initiate a dictionary to store column dictionaries
        col_count = {} #col_count[column_index][column_number]: frequency ; we track the frequency of the numbers in each column
        square_count = {} #square_count[coordinate]: frequency ; track the frequency of the numbers in each square of the board (3x3)
        for r_index, r in enumerate(board):
            r_count = {}
            for c_index, c in enumerate(r):
                if c not in r_count and c != ".":
                    r_count[c] = 1
                elif c in r_count: 
                    return False

                if c_index not in col_count:
                    col_count[c_index] = {}
                if c not in col_count[c_index] and c != ".":
                    col_count[c_index][c] = 1
                elif c in col_count[c_index]:
                    return False

                coor = str(r_index // 3) + str(c_index // 3)
                if coor not in square_count:
                    square_count[coor] = {}
                if c not in square_count[coor] and c != ".":
                    square_count[coor][c] = 1
                elif c in square_count[coor]:
                    return False

        # Time complexity: O(m), the size of the board is fixed, and we only iterate each row once
        # Space complexity: O(m), idk
        return True