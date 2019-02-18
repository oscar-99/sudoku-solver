# This file will be used to implement everything for the mk4 functional solver
import utilities
import numpy as np

def strategymk4(board, print_results=False):
    """
    The light weight mk4 solver.

    Parameters:
        board (np.array): a 9 by 9 array corresponding to the original board
    """

    # Solve as far as possible directly through logic
    stuck = False
    while not stuck:
        # Check if board is full
        if check_full(board):
            return board

        # Solve logically. When at least one possibility can be found we are not stuck
        stuck = True
        for i in range(9):
            for j in range(9):
                if board[i,j] == 0:
                    possibilities = [k for k in range(10) if k in 
                    get_column_numbers(j, board) and get_row_numbers(i, board) and get_square_numbers(i, j, board)]

                    if len(possibilities) == 1:
                        board[i,j] = possibilities[0]
                        stuck = False
                    
    # Save a copy of the logically filled board
    original_board = board.copy()
    i, j = 0, 0 
    while True:
        # If we are on clue go to next
        if original_board[i, j] != 0:
            if j == 8:
                j = 0
                i += 1
            else:
                j += 1

            continue

        # Try to find valid entry
        while board[i,j] < 10:
            board[i,j] += 1
            
            if print_results:
                    print(board)

            if check_correct(i, j, board) and board[i,j]<10:
                if j == 8:
                    j = 0
                    i += 1
                else:
                    j += 1

                break
            
        # If valid entry can't be found we must backtrack      
        else:
            # Set to zero and backtrack to last entered result.
            board[i,j] = 0
            if print_results:
                print(board)
        
            found = False
            while not found:
                # Find a added point
                if j > 0:
                    j -= 1
                else:
                    i -= 1
                    j = 8

                if original_board[i,j] == 0:
                    found = True

        # Check to exit loop once reached last row.           
        if check_full(board):
            if check_full_correct(board):
                return board
                    
    


def get_row_numbers(row, board):
    """
    Method for getting missing numbers along a row.

    Parameters:
        row (int): The row to get missing numbers from.

    Returns:
        (list): List of numbers missing. 
    """
    return [i for i in range(1,10) if i not in board[row, :]]


def get_column_numbers(column, board):
    """
    Method for getting missing numbers along a column.

    Parameters:
        column (int): The column to get missing numbers from.

    Returns:
        (list): List of numbers missing. 
    """
    return [i for i in range(1,10) if i not in board[:,column]]


def get_square_numbers(row, column, board):
    """
    Method for getting missing numbers in a 3x3 square.

    Parameters:
        square (int): The square to get missing numbers from.

    Returns:
        (list): List of missing numbers 
    """
    subsquare_row = row // 3
    subsquare_column = column // 3
    subsquare = board[subsquare_row*3: (subsquare_row + 1)*3, subsquare_column*3: (subsquare_column + 1)*3]

    return [i for i in range(1, 10) if i not in subsquare]


def check_row(row, board):
    """
    Function to check along the row of a board and return False if row is invalid (contains at least one number more than once), True if valid.
    """
    for i in range(1, 10):
        if np.count_nonzero(board[row,:] == i) > 1:
            return False

    return True

def check_column(column, board):
    """
    Function to check along the column of a board and return False if row is invalid (contains at least one number more than once), True if valid
    """
    for i in range(1, 10):
        if np.count_nonzero(board[:,column] == i) > 1:
            return False

    return True

def check_square(row, column, board):
    """
    Function to check a subsquare of a board and return False if row is invalid (contains at least one number more than once), True if valid
    """
    # Get the subsquare corresponding to the row and column
    subsquare_row = row // 3
    subsquare_column = column // 3
    subsquare = board[subsquare_row*3: (subsquare_row + 1)*3, subsquare_column*3: (subsquare_column + 1)*3]
    
    for i in range(1, 10):
        if np.count_nonzero(subsquare == i) > 1:
            return False

    return True

def check_correct(row, column, board):
    """
    Function to check a single square is valid
    """
    return (check_row(row, board) and check_column(column, board) and check_square(row, column, board))
        

def check_full_correct(board):
    """
    Function to check if the entire board is correct. Only need to check row column or square.
    """

    for i in range(9):
        if not check_row(i, board):
            return False
    
        if not check_column(i, board):
            return False

    for i in range(3):
        for j in range(3):
            if not check_square(i*3, j*3, board):
                return False


    return True


def check_full(board):
    """
    Check if board is full. Return True if board is full (no zeros) and False if not full.
    """
    for i in range(9):
        for j in range(9):
            if board[i,j] == 0: 
                return False

    return True
