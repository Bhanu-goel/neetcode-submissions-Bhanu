def checkrow(num,board,row):
    if num == ".":
        return True
    if board[row].count(num) > 1:
        return False
    return True

def checkcol(num,board,col):
    if num == ".":
        return True
    colelem = [i[col] for i in board]
    if colelem.count(num) > 1:
        return False
    return True

def checkbox(num,board,row,col):
    if num == ".":
        return True
    start_row = (row//3)*3
    start_col = (col//3)*3

    count = 0
    for i in range(start_row,start_row+3):
        for j in range(start_col,start_col+3):
            if board[i][j] == num:
                count+=1
    
    if count > 1:
        return False
    return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if not checkrow(num,board,i):
                    return False
                if not checkcol(num,board,j):
                    return False
                if not checkbox(num,board,i,j):
                    return False
        return True