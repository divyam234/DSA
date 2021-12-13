#https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int):
        
        def check_bound(r,c):
            return 0 <= r < n and 0 <= c < n
            
        def isValid(r,c):
            for i in range(r):
                if board[i][c]=='Q':
                    return False
                
            for i in range(1,r+1):
                if not check_bound(r-i,c-i):
                    break
                if board[r - i][c - i] == 'Q':
                    return False 
            
            for i in range(1,r+1):
                if not check_bound(r-i,c+i):
                    break
                if board[r - i][c + i] == 'Q':
                    return False 
            return True
                
            
        def solve(r):
            if r==n:
                ans.append([''.join(i) for i in board])
                return

            for c in range(n):
                if isValid(r,c):
                    board[r][c]='Q'
                    solve(r+1)
                    board[r][c]='.'
                
        ans=[]
        board=[['.']*n for i in range(n)]
        solve(0)
        return ans
            
        