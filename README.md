<h2><b>The Puzzle</b></h2>

<p>
    Sudoku is a puzzle based on a 9 by 9 grid of numbers. The puzzle is solved by filling each row, column and 3 by 3
    subsquare with the numbers 1 to 9 beginning from a set of pre-filled numbers called clues. Some sudoku puzzles can
    be solved through a direct logical process whereby possibilities in each square are
</p>

<h2><b>Objectives</b></h2>

<p>
    The aim of the project is to solve a set of 50 sudoku puzzles some of which are not solvable with direct logic along with a UI for solving the puzzles manually.
</p>

<h2><b>Implementation</b></h2>

<p>
    An object oriented approach was taken for the project and it was broken up into several elements and files. 
    <ul>
        <li>
            boardui.py implements a ui .
        </li>
        <li>
            sudoku.py implements a model of the board.
        </li>
        <li>
            strategy.py implements several solving strategy algorithms.
        </li>
        <li>
        utilities.py has a several utility functions for formating puzzles and coordinate transforms.
        </li>
        <li>
            newstrat.py implements strategymk4 in a new functional framework.
        </li>
        <li>
            timing.py implements timing for each of the strategies.
        </li>
    </ul>
</p>

<h3><b>The UI </b></h3>

The UI is implemented in the tkinter package for python.

<h3><b>The board</b></h3>

The sudoku board is implemented as the SudokuBoard object, which modelled the sudoku board as a 9 by 9 array along with methods to interact with the board. The original board object interfaces with the UI and the strategy objects and so it also store a history of the board.


<h3><b>Strategy</b></h3>

There were several implementations of the strategy for solving the problem.


<h3><b>strategymk1</b></h3>

The mark 1 strategy is a basic implementation of a basic object oriented logical solver. The method searches through the grid to find the possible solutions for each grid, if only one possibility is found for a square it enters and searches again.

    
<h3><b>strategymk2</b></h3>

The mark 2 strategy is a solver that implemented a object oriented brute force algorithm. The brute force method works by having each empty square would be guessed to contain a 1 until a contradiction was found at which point the algorithm would return to the last guessed square and add one. If a square could not fit any value from 1-9 then the cell was reset to empty and the last guess had one added.


<h3><b>strategymk3</b></h3>

The mark 3 algorithm is an object oriented mix of the last two marks. The method intends to directly logically solve the board until it there are no single possibilities left at which point it switches to logical guessing. That is, the method takes a square with multiple possibilities and guesses the value, storing the state of the board as well as the other possibilities in a Guess object. The method then logically solves from the guess until the board is either solved, a contradiction is found, or another guess has to be made. In the case of a contradiction being found the board reverts to the last guess and tries the next possibility.


<h3><b>strategymk4</b></h3>

The aim of the strategymk4 algorithm is to re-implement the brute force mark 2 algorithm but drop the integration with UI, move to a functional paradigm and make efficiency improvements to the algorithms. The algorithm also makes use of a basic mark 1 type logical solver to speed the algorithm by only starting brute force when the logical method breaks down and a guess is required.  
