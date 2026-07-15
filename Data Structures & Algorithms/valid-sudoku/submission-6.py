class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_count = {} #col_count[c_index][col] : frequency
        square_count = {}
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
        return True