from sudoku import SudokuBoard
from boardui import BoardGUI
from strategy import StrategyMk1
import utilities

utilities.puzzle_import(50)
sum = 0
for i in range(1, 50):
    puzzle_number = i
    board = utilities.generate_puzzle_matrix(puzzle_number)
    game = SudokuBoard(board, puzzle_number)
    strat = StrategyMk1(game)
    strat.solver()
    sum += strat.game.get_top_sum()