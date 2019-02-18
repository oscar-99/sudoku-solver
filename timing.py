from sudoku import SudokuBoard
from boardui import BoardGUI
from strategy import StrategyMk1, StrategyMk2, StrategyMk3, Guess
from newstrat import strategymk4
import utilities
import time

boards = []
for i in range(1,11):
        puzzle_number = i
        boards.append(utilities.generate_puzzle_matrix(puzzle_number))

def solve4(boards):
    for n, board in enumerate(boards):
        print(n)
        strategymk4(board)

def solve3(boards):
    for n, board in enumerate(boards):
        print(n)
        game = SudokuBoard(board,n)
        strat = StrategyMk3(game)
        strat.solve()

def solve2(boards):
    for n, board in enumerate(boards):
        print(n)
        game = SudokuBoard(board, n)
        strat = StrategyMk2(game)
        strat.solve()
    

# Check 3 and 13

print("Method 2")
start2 = time.time()
solve2(boards)
print("Method 2 Results: {}".format(time.time() - start2))



