from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_dicts = {
            0: {},
            1: {},
            2: {},
            3: {},
            4: {},
            5: {},
            6: {},
            7: {},
            8: {},
        }
        square_sets = {
                "00": {},
                "01": {},
                "02": {},
                "10": {},
                "11": {},
                "12": {},
                "20": {},
                "21": {},
                "22": {},
            }
        for r, row in enumerate(board):
            dict_row = {}
            for i, digit in enumerate(row): 
                if digit != "." and digit not in col_dicts[i]:
                    col_dicts[i][digit] = 1
                elif digit in col_dicts[i]:
                    return False

                if digit != "." and digit not in dict_row: 
                    dict_row[digit] = 1
                elif digit in dict_row:
                    return False

                x = r // 3
                y = i // 3
                coor = str(x) + str(y)
                if digit != "." and digit not in square_sets[coor]:
                    square_sets[coor][digit] = 1
                elif digit in square_sets[coor]:
                    return False
        return True    
        
