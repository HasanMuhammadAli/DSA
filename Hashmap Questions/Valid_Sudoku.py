'''
Name: Muhammad Ali Mosin Hasan
Date: 15/6/25
Problem: 36: Valid Sudoku
'''

def isValidSudoku(board):
    '''
    Checks if a given Sudoku board is valid.

    Args:
        board (list[list[str]]): 9x9 Sudoku board represented as a list of lists.

    Returns:
        bool: True if the board is valid, False otherwise.
    '''
    #validate rows
    for i in range(9):
        s = set()
        for j in range(9):
            item = board[i][j]
            if item in s:
                return False
            elif item != '.':  
                s.add(item)
    
    #validate columns
    for i in range(9):
        s = set()
        for j in range(9):
            item = board[j][i]
            if item in s:
                return False
            elif item != '.':
                s.add(item)
    
    #validate Boxes
    starts = [(0, 0), (0, 3), (0, 6),
              (3, 0), (3, 3), (3, 6),
              (6, 0), (6, 3), (6, 6)]
    
    for i, j in starts:
        s = set()
        for row in range(i, i + 3):
            for col in range(j, j + 3):
                item = board[row][col]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)
    return True

# Example usage
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", "6", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
# Test the function
is_valid = isValidSudoku(board)
print("Is the Sudoku board valid? " + str(is_valid))
