class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        def check(x,y):
            r_set = set(board[x])
            c_set = set([board[c][y] for c in range(9)])
            b_set = set([board[x//3*3+c][y//3*3+r] for c in range(3) for r in range(3)])
            return ( r_set | c_set | b_set )# - set(['.'])
        
        def solve(board):
            for c in range(9):
                for r in range(9):
                    if board[c][r] == '.':
                        for tn in list(set("123456789")-check(c,r)):
                            board[c][r] = tn
                            if solve(board):
                                return True
                            else:
                                board[c][r] = '.'
                        return False
            return True

        solve(board)


if __name__ == '__main__':
    s = Solution()
    board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
    boardnew = [list(i) for i in board]
    s.solveSudoku(boardnew)
    
    print("The input Sudoku:\n")
    print("\n".join([" ".join(i) for i in board]),end='\n\n')

    print ("The solved Sudoku:\n")
    print("\n".join([" ".join(i) for i in boardnew]),end='\n\n')
