import os
import numpy as np

def puzzle_import(n):
    """"
    Function for importing a specific puzzle to a text file in the "puzzles" folder.

    Parameters:
        n (int): Puzzle number. 
    """
    OPEN_PATH = os.path.join("Sudoku Solver", "p096_sudoku.txt")
    # Comparison with puzzle number will be string based
    if n < 10:
        n = "0" + str(n)
    else:
        n = str(n)

    with open(OPEN_PATH, "r") as sudoko_puzzles:
        sudoko_puzzles_read = sudoko_puzzles.read()
        sudoko_puzzles_list = sudoko_puzzles_read.split("Grid")
        selected_puzzle_str = None

        # Select puzzle.
        for puzzle_str in sudoko_puzzles_list:
            if puzzle_str[1:3] == n:
                selected_puzzle_str = puzzle_str
        
        # Check if puzzle is selected.
        if selected_puzzle_str is None:
            raise ValueError("Selected puzzle is not in puzzle set.")
    
    # Puzzle will be stored as txt file
    file_name = "puzzle" + n
    with open(os.path.join("Sudoku Solver", "puzzles",file_name), "w") as save_file:
        selected_puzzle_list = selected_puzzle_str.split("\n")
        selected_puzzle_list = selected_puzzle_list[1:-1]
        for row in selected_puzzle_list:
            row_list = []
            for number in row:
                row_list.append(number)
            save_file.write(",".join(row_list))
            save_file.write("\n")


def generate_puzzle_matrix(n):
    """
    Generates a puzzle matrix.

    Parameters:
        n (int): The puzzle number to get 
    """
    if n < 100:
        if n < 10:
            n = "0" + str(n)
        else:
            n = str(n)
    return np.genfromtxt(os.path.join("Sudoku Solver","puzzles","puzzle"+n),delimiter=",")


def coords_to_square(row, column):
    """
    Takes in coordinate (with top left as origin) on sudoku grid and gives the larger subsquare the coordinate lies in.

    Parameters:
        row (int): The row coordinate of the point.
        column (int): The column of the point.

    Returns:
        square (int): The 3x3 subsquare the point belongs to.
    """

    subsquare_column = column // 3 +  1
    subsquare_row = row // 3 + 1
    if subsquare_row == 1:
        return subsquare_column
    elif subsquare_row == 2:
        return subsquare_column + 3
    else:
        return subsquare_column + 6

    

