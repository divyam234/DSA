#https://leetcode.com/problems/sudoku-solver/

from itertools import product

class Solution:
    found=False
    def solveSudoku(self, board):
        
        def checkPresence(r,c,n):
            x,y=r//3*3,c//3*3
            for i,j in product(range(x,x+3),range(y,y+3)):
                if board[i][j] ==str(n):
                    return True
            return False
        
        
        def isValid(r,c,n):
            
            for i in range(9):
                if board[i][c] ==str(n):
                    return False
                
            for i in range(9):
                if board[r][i] == str(n):
                    return False   
            return True
        
        def solve(r,c):
            if r==9:
                self.found=True
                return
            
            if c > 8:
                solve(r+1,0)
            
            elif board[r][c]!='.':
                    solve(r,c+1)
            else:
                for state in range(1,10):
                    if  not checkPresence(r,c,state) and isValid(r,c,state):
                        board[r][c] =str(state)
                        solve(r,c+1)
                        if not self.found:
                            board[r][c] ='.'
                        else:
                            return
        solve(0,0)