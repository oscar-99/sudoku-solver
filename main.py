from sudoku import SudokuBoard
from boardui import BoardGUI
from strategy import StrategyMk1, StrategyMk2, StrategyMk3
import utilities


sum = 0

puzzle_number = 1
board = utilities.generate_puzzle_matrix(puzzle_number)
game = SudokuBoard(board, puzzle_number)
strat = StrategyMk3(game)
print(game.original_board)
strat.solve(print_board=True)
sum += strat.game.get_top_sum()

print(sum)