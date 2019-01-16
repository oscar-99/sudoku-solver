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
            row_missing = self.game.board.get_row_numbers(i)
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
    This strategy aims to implent a strategy that can deal with non logical solutions. 
    """
    pass      


        
