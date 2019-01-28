# Deals with strategy for solving sudoku board.
import numpy as np
import utilities as utilities

class StrategyMk1(object):
    """
    Class for implementing the mk1 strategy. This strategy can solve puzzles which are solvable with direct logic i.e. no guessing. 
    """
    def __init__(self, game):
        self.game = game
        self.solution_matrix = []


    def search_grid(self):
        """
        Method that searches the grid by square, by row and then by column to find potential entries. 

        Generates a list of lists of lists. Where the two outer lists represent the grid and inner represents the possibilities for a given square.  
        """
        self.solution_matrix = []
        for i in range(9):
            solution_row = []
            row_missing = self.game.get_row_numbers(i)
            for j in range(9):
                if self.game.board[i][j] == 0:
                    column_missing = self.game.get_column_numbers(j)
                    square_missing = self.game.get_square_numbers(utilities.coords_to_square(i,j))
                    position_missing = [i for i in range(1, 10) if i in row_missing and i in column_missing and i in square_missing]
                    solution_row.append(position_missing)
                else: solution_row.append([])
            self.solution_matrix.append(solution_row)



    def step(self):
        """
        Method that searches grid to find missing numbers and enter them in. Returns true if at least one square is found. 
        """
                     
        self.search_grid()

        for i in range(9):
            for j in range(9):
                if len(self.solution_matrix[i][j]) == 1:
                    self.game.add_cell((i,j), self.solution_matrix[i][j][0])
                    return True
        
        print("No move found")
        print(self.game.board)
        print(self.solution_matrix)
        return False

    
    def solver(self):
        """
        Solver steps forward to find solution.
        """

        while self.step():
            if self.game.check_board_full():
                if self.game.check_board():
                    print("Solved: \n")
                    print(self.game.board)
                    sum = self.game.get_top_sum()
                    print("Concaternated top corner = ", sum)
                else: 
                    print("Solution incorrect.")
                    print(self.game.board)
                break


class StrategyMk2(object):
    """
    A strategy to implement a brute force algorithm. The algorithm will work by guessing the values and then backtracking. 
    """

    def __init__(self, game):
        self.game = game


    def search_board(self):
        """
        A function for finding an empty spot on the board and placing 1 in the first spot found. 
        """

        for i in range(9):
            for j in range(9):
                if self.game.board[i][j] == 0:
                    self.game.add_cell((i, j), 1)
                    return [i, j]


    def find_prev_point(self, point):
        """
        Method to find a previous point to modify.

        point (list<int>): Coordinate of the current point. Will find a point       behind current point.
        """
        found = False
        while not found:
            # Find a added point
            if point[1] > 0:
                point[1] -= 1
            else:
                point[0] -= 1
                point[1] = 8
            
            entry = self.game.board[point[0]][point[1]] 
            if self.game.original_board[point[0]][point[1]] == 0:
                self.game.remove_cell(point)
                if entry < 9:    
                    self.game.add_cell(point, entry + 1)
                    found = True


    def solve(self, print_result=False):
        """
        A pure brute force algorithm.

        Parameters:
            print_result (boolean): If true will print the result of each step
        """

        while not (self.game.check_board_full() and self.game.check_board()):
            if self.game.check_board():
                # Check if board is valid and add a 1.
                last_point = self.search_board()

            else:
                # If board is not valid take the last added point and remove it.
                value = self.game.board[last_point[0]][last_point[1]]
                self.game.remove_cell(last_point)
                if value < 9:
                    # If removed value is less than 9 try next value.
                    self.game.add_cell(last_point, value + 1)

                else:
                    # Otherwise all points have been tried and last added point needs to be changed.         
                    self.find_prev_point(last_point)

            if print_result:
                print(self.game.puzzle_number)
                print(self.game.board)


class StrategyMk3(object):
    """
    This strategy aims to implent a strategy that can deal with sudoku puzzles which are not directly solvable. This will be done using a brute force method. 
    """

    def __init__(self, game):
        self.game = game
        self.solution_matrix = []

        # The guess matrix will contain unknown values for the last certain board. i.e. a board with no guesses
        self.guess_matrix = []
        for _ in range(9):
            row = []
            for __ in range(9):
                row.append([])
            self.guess_matrix.append(row)

        
        # The guess list tracks where guesses have been made.
        self.guess_list = []
        # Define a check matrix which tracks values that have been checked.
        self.check_matrix = []
        for _ in range(9):
            row = []
            for __ in range(9): 
                row.append([])
            self.check_matrix.append(row)
 

        
    def search_grid(self):
        """
        Method that searches the grid by square, by row and then by column to find potential entries. 

        Generates a list of lists of lists. Where the two outer lists represent the grid and inner represents the possibilities for a given square.  
        """
        self.solution_matrix = []
        for i in range(9):
            solution_row = []
            row_missing = self.game.get_row_numbers(i)
            for j in range(9):
                if self.game.board[i][j] == 0:
                    # Generate the missing numbers and list of checked guesses.
                    column_missing = self.game.get_column_numbers(j)
                    square = utilities.coords_to_square(i,j)
                    square_missing = self.game.get_square_numbers(square)
                    checked = self.check_matrix[i][j]
                    
                    # Find possible numbers.
                    position_missing = [i for i in range(1, 10) if (i in row_missing and i in column_missing and i in square_missing and i not in checked)]
                    solution_row.append(position_missing)

                else: 
                    solution_row.append([])

            self.solution_matrix.append(solution_row)

    
    def logic_fill(self):
        """
        Aim of this method is to fill in directly solvable squares.
        """
        for i in range(9):
            for j in range(9):
                if len(self.solution_matrix[i][j]) == 1:
                    self.game.add_cell((i,j), self.solution_matrix[i][j][0])
                    return True

        return False


    def generate_guess_matrix(self):
        """
        Method for generation of possibilities from the last certain position.
        """
        self.guess_matrix = []
        for i in range(9):
            guess_row = []
            for j in range(9):
                self.search_grid()
                possibility_list = self.solution_matrix[i][j]
                if len(possibility_list) > 1:
                    guess_row.append(possibility_list)
                else:
                    guess_row.append([])

            self.guess_matrix.append(guess_row)
    

    def guess(self):
        """
        Method for implementing a guess. 
        """
        for i in range(9):
            for j in range(9):
                if self.game.board[i][j] == 0:
                    possibilities = self.guess_matrix[i][j]
                    self.guess_list.append(Guess((i,j), possibilities, self.game.board))
                    return True

        return False

    
    def backtrack(self):
        """
        Method to handle the backtrack algorithm. Method will backtrack (deleting bad results) to last guess and increment or further backtrack until an increment is found.
        """

        while True:
            # Set the last guess to the last guess and set the board to the state at that board.
            last_guess = self.guess_list[-1]
            self.game.set_board(last_guess.board)

            # If length is one 
            if len(self.guess_list) == 1:
                self.check_matrix[last_guess.coord[0]][last_guess.coord[1]].append(last_guess.value)
                last_guess.next_possibility()
                return

            if last_guess.next_possibility():
                # If there is another possibility for guess we are done, update the board
                self.game.add_cell(last_guess.coord, last_guess.value)
                return

            else: 
                # If there is no next possibility remove last guess from list of guesses.
                self.guess_list.pop(-1)

        
    def solve(self, print_board=False):
        """
        The solving algorithm for mk3 strategy.
        """

        while not (self.game.check_board_full() and self.game.check_board()):
            # Update guess matrix. 
            if len(self.guess_list) == 0:
                self.generate_guess_matrix()

            if self.game.check_board():
                # This solves directly solvable squares
                self.search_grid()
                if not self.logic_fill():
                    # Deal with if not fully logically filled
                    # Run guess
                    if self.guess():
                        self.game.add_cell(self.guess_list[-1].coord, self.guess_list[-1].value)
                          
            if not self.game.check_board():
                self.backtrack()
                    
            if print_board:
                print(self.game.puzzle_number)
                print(self.game.board)


class Guess(object):
    """
    An object to model a guess.
    """
    def __init__(self, coord, possibilities, board):
        """
        Parameters:
            coord (tuple): Coord is tuple corresponding to coordinate.
            possibilities (list): The possible values for the guess.
            board (np.array): The board before guess was made.
        """
        self.coord = coord
        self.possibilities = possibilities
        self.index = 0
        self.value = self.possibilities[self.index]
        self.board = board

    def next_possibility(self):
        """
        Method which advances the guess.
        """
        self.index += 1
        try:
             self.value = self.possibilities[self.index]
             return True

        except IndexError:
            return False
        

                                      


                
                




        
