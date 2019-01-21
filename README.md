# Sudoku-Solver

Sudoku solver project for solving project euler problem 96.

## Objectives
Aim is to implement several different strategies to solve the 50 puzzles. 
1. Puzzles can be timed to compare the speed of different strategies.
2. Implement a UI for both normal solving of puzzles and showing the process of solving.
3. UI will be reimplimented in JS in order to have it work web based.  

## Files
* sudoku.py is a file containing the implementation of the SudokuBoard class. This involves management of boards, storage of board history as well as methods for modifying and getting information about boards.
* strategy.py is a file containing the implementation of the strategy classes.
  * Strategymk1 is a direct logic strategy.
  * Strategymk2 is a brute force solve strategy. 
* boardui.py is python implementation of UI in tkinter.
* utilities.py is a file containg a set of utility functions for loading in data etc.
  