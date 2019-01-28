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
        self.clear_history()
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
            self.clear_history()
            return True

        self.clear_history()
        return False

    def erase_ahead_coord(self, coord):
        """
        Method which deletes all previously entered points ahead of and including the coord.

        Parameters:
            coord (tuple): The coordinate of the cell.
        """
        # In first deletion row only remove past the column number
        for k in range(coord[1], 9):
            if self.original_board[coord[0]][k] == 0:
                self.remove_cell((coord[0], k))

        # Past the specific row delete all
        for i in range(coord[0]+1, 9):
            for j in range(9):
                if self.original_board[i][j] == 0:
                    self.remove_cell((i,j))

    
    def set_board(self, board):
        """
        Method which sets the current board to an input board.
        """
        self.board_history.append(board)
        self.board = board
        self.clear_history()


    def clear_history(self):
        """
        Clear the history of the board once board is large i.e. >100
        """
        if len(self.board_history) >= 100:
            self.board_history.pop(0)
                    

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

    
    def check_board(self):
        """
        This method wil move through a board checking all rows, columns and square to be valid (i.e. not having more that two occurances). Returns False if an invalid row, column or square is found. True otherwise. 
        """
        # Check rows
        for i in range(9):
            for num in range(1, 10):
                if self.board[i].tolist().count(num) > 1:
                    return False

        # Check columns
        for i in range(9):
            column = []
            for j in range(9):
                column.append(self.board[j][i])
           
            for num in range(1, 10):
                if column.count(num) > 1:
                    return False
        
        squares = self.get_sub_squares()
        # Check squares:
        for i in range(1, 10):
            square = squares[i]
            square = square.flatten().tolist()
            for num in range(1, 10):
                if square.count(num) > 1:
                    return False

        return True


    def get_top_sum(self):
        """ Method for project euler. Gets top three numbers. """
        num = ""
        for i in range(3):
            num += str(int(self.board[0][i]))

        return int(num)


    def get_row_numbers(self, row):
        """
        Method for getting missing numbers along a row.

        Parameters:
            row (int): The row to get missing numbers from.

        Returns:
            (list): List of numbers missing. 
        """
        return [i for i in range(1,10) if i not in self.board[row]]


    def get_column_numbers(self, column):
        """
        Method for getting missing numbers along a column.

        Parameters:
            column (int): The column to get missing numbers from.

        Returns:
            (list): List of numbers missing. 
        """
        column_list = []
        for i in range(9):
            column_list.append(self.board[i][column])

        return [i for i in range(1,10) if i not in column_list]


    def get_square_numbers(self, square):
        """
        Method for getting missing numbers in a 3x3 square in following number scheme:
            1 2 3
            4 5 6
            7 8 9

        Parameters:
            square (int): The square to get missing numbers from.

        Returns:
            (list): List of missing numbers 
        """
        square = self.get_sub_squares()[square]
        square = square.flatten().tolist()
        return [i for i in range(1, 10) if i not in square]

        

        



   