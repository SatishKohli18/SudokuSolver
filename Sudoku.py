class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        row,col = -1,-1
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    row = i
                    col = j
        if row == -1 :
            return True
        for num in ([str(i) for i in range(1,10)]):
            if self.isSafe(board,row, col, num):
                board[row][col] = num
                if self.solveSudoku(board):
                    return True
                board[row][col] = "."
        return False
            
    def isSafe(self,board, row, col, ch):
        boxrow = row - row%3
        boxcol = col - col%3
        if self.checkrow(board,row,ch) and self.checkcol(board,col,ch) and self.checksquare(board,boxrow, boxcol, ch):
            return True
        return False
    
    def checkrow(self, board,row, ch):
        for col in range(9):
            if board[row][col] == ch:
                return False
        return True
    
    def checkcol(self,board, col, ch):
        for row in range(9):
            if board[row][col] == ch:
                return False
        return True
       
    def checksquare(self,board, row, col, ch):
        for r in range(row, row+3):
            for c in range(col, col+3):
                if board[r][c] == ch:
                    return False
        return True
                    

    
