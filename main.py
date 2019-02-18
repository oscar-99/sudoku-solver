from sudoku import SudokuBoard
from boardui import BoardGUI
import tkinter as tk
from strategy import StrategyMk1, StrategyMk2, StrategyMk3
from newstrat import strategymk4
import utilities

board = utilities.generate_puzzle_matrix(3)
game = SudokuBoard(board, 3)

window = tk.Tk()
BoardGUI(window,game )


tk.mainloop()


