from sudoku import SudokuBoard
from boardui import BoardGUI
from strategy import StrategyMk1
import utilities


sum = 0

puzzle_number = 1
board = utilities.generate_puzzle_matrix(puzzle_number)
game = SudokuBoard(board, puzzle_number)
strat = StrategyMk1(game)
strat.solver()
sum += strat.game.get_top_sum()


