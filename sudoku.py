# For the sudoku game implementation.
import numpy as np

class SudokuBoard(object):
    """
    A representation of a sudoku board. 
    """

    def __init__(self, board, puzzle_number):
        """
        Initializes a sudoku board.
        
        Parameters:
            board (np.array): A 9x9 numpy array object that represents the sudoku board
        """

        self.original_board = board
        self.board = board
        self.board_history = [board]
        self.move_count = 0
        self.puzzle_number = puzzle_number


    def add_cell(self, coord, num):
        """
        Method to update a cell value and update boards.

        Parameters:
            coord (tuple): The coordinate of the cell.
            num (int): The new value.
        """
        if (self.board[coord[0], coord[1]] == 0 and 
        self.original_board[coord[0], coord[1]] == 0):
            # Create new board and move into board history.
            new_board = self.board.copy()
            new_board[coord[0], coord[1]] = num

            # This way moves can be overwritten
            self.move_count += 1
            self.board_history.insert(self.move_count, new_board)
            self.board = new_board

            # Delete all boards ahead of the new board
            del(self.board_history[self.move_count + 1:])
            return True
        
        return False


    def remove_cell(self, coord):
        """
        Removes an added number from the board.

        Parameters:
            coord (tuple): The coordinate of the cell.
        """
        # Check if cell selected is not original cell and has a number
        if (self.board[coord[0], coord[1]] != 0 and 
        self.original_board[coord[0], coord[1]] == 0):
            self.move_count +=1
            new_board = self.board.copy()
            new_board[coord[0], coord[1]] = 0
            self.board_history.insert(self.move_count, new_board)
            self.board = new_board
            return True

        return False


    def clear(self):
        """ Clears the game and restores original board. """
        self.board = self.original_board
        self.board_history = [self.original_board]
        self.move_count = 0


    def get_sub_squares(self):
        """
        Method that gives the 3x3 subsquares for the current sudoku board in a dictionary of numpy arrays. Subsquares keys in the dictionary are labeled according to:
            1 2 3
            4 5 6
            7 8 9

        Parameters:
            square (int): The square needed.
        """
        square_dict = {}
        square_no = 1

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                a = self.board[:][i:i+3]
                square_dict[square_no] = np.transpose(np.transpose(a)[:][j:j+3])
                square_no += 1

        return square_dict

    
    def check_board_full(self):
        """
        Checks if a board is full.
        """
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return False

        return True

    
    def check_solution(self):
        """
        Check a solution.
        """
        # Check rows
        for i in range(9):
            for num in range(1, 10):
                if num not in self.board[i]:
                    return False

        # Check columns
        for i in range(9):
            column = []
            for j in range(9):
                column.append(self.board[j][i])

            for num in range(1, 10):
                if num not in column:
                    return False
        
        squares = self.get_sub_squares()
        # Check squares:
        for i in range(1, 10):
            square = squares[i]
            square = square.flatten().tolist()
            for num in range(1, 10):
                if num not in square:
                    return False

        return True

    def get_top_sum(self):
        """ Method for project euler. Gets top three numbers. """
        num = ""
        for i in range(3):
            num += str(int(self.board[0][i]))

        return int(num)

        

        



   