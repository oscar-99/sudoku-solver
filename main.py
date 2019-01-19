from sudoku import SudokuBoard
from boardui import BoardGUI
from strategy import StrategyMk1, StrategyMk2, brute_force_algorithm
import utilities


sum = 0

puzzle_number = 40
board = utilities.generate_puzzle_matrix(puzzle_number)
game = SudokuBoard(board, puzzle_number)
strat = StrategyMk2(game)

print(game.original_board)
strat.solve(True)

sum += strat.game.get_top_sum()