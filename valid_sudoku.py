from typing import List
import argparse
from loguru import logger


"""

NAME : Valid Sudoku
LINK :
https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/769/

DESC:
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be 
validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without 
repetition.

"""
def isValidSudoku(board: List[List[str]]) -> bool:
    
    """
    DOCTEST
    >>> board = [
      ["5","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]
    ]
    True

    >>> board = [
      ["8","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]
    ]
    False
    """
    col = 9
    row = 9
    for j in range(col):
        d = {}
        res = True
        for i in range(row):
            if board[j][i] != '.':
                if (d.get(board[j][i]) != None):
                    res = False
                    return res
                d[board[j][i]] = 1
    for i in range(row):
        d = {}
        res = True
        for j in range(col):
            if board[j][i] != '.':
                if (d.get(board[j][i]) != None):
                    res = False
                    return res
                d[board[j][i]] = 1
   
    for ii in range(3):
        for jj in range(3):
            
            d = {}
            for i in range(ii*3, 3*(ii+1)):
                res = True
                for j in range(jj*3, 3*(jj+1)):
                    if board[j][i] != '.':
                        if (d.get(board[j][i]) != None):
                            res = False
                            return res
                        d[board[j][i]] = 1
           
    return res
if __name__ == "__main__":
    parser = argparse.ArgumentParser
    parser.addargument('--board', nargs='+',
                        help='A 9x9 Sudoku board',
                        required=True)
    board = parser.parse_args().board

    logger.info(f'Got array from command line arguments : {board}')
    logger.info(f'Determine a Sudoku board is valid ...')

    res = isValidSudoku(board)
    logger.info(f'...Done')

    print('Result :', res)