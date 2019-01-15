import tkinter as tk
from tkinter import messagebox

class BoardGUI(tk.Frame):
    """A GUI for the sudoku board"""

    def __init__(self, parent, game):
        """
        Initializes board ui
        """
        self.game = game
        self.parent = parent
        tk.Frame.__init__(self, parent)
        
        # Height and width of sudoku board.
        self.WIDTH = 500
        self.HEIGHT = 500
        # Margin around board
        self.MARGIN = 25
        self._init_ui()

        self.cell_highlighted = None


    def _init_ui(self):
        """
        Initialize whole ui, games space and game controls
        """
        self.parent.title("Sudoku")
        self.pack(fill=tk.BOTH, expand=1)

        # Initialize canvas
        self.canvas = tk.Canvas(width=self.WIDTH + self.MARGIN, height=self.HEIGHT + self.MARGIN)
        self.canvas.pack(fill = tk.BOTH, side=tk.LEFT)
        self.canvas.bind("<Button-1>", self._left_click)
        self.canvas.bind("<Key>", self._key_press)
        self.canvas.bind("<BackSpace>", self._backspace)
        
        # Control Panel
        self.controls = tk.Frame(self.parent)
        self.controls.pack(side=tk.LEFT)
        puzzle_label = tk.Label(self.controls, text="Puzzle Number: " + str(self.game.puzzle_number))
        puzzle_label.pack(side=tk.TOP)

        # Undo and redo buttons.
        undo_redo_button = tk.Frame(self.controls)
        undo_redo_button.pack(side=tk.TOP)
        self.undo_button = tk.Button(undo_redo_button, text="Undo",        state="disabled", command=self._undo)
        self.undo_button.pack(side=tk.LEFT)
        self.redo_button = tk.Button(undo_redo_button, text="Redo", command=self._redo)
        self.redo_button.pack(side=tk.LEFT)

        # Clear and new puzzle.
        clear_button = tk.Button(self.controls, text="Clear Game", command=self._clear)
        clear_button.pack(side=tk.TOP)
        new_puzzle = tk.Button(self.controls, text="New Puzzle", command=self._new_puzzle)
        new_puzzle.pack(side=tk.TOP)

        # Draw to canvas
        self._draw_grid()
        self._draw_puzzle(self.game.board)


    def _draw_grid(self):
        """
        Draws sudoku grid.
        """
        colour = "black"
        for i in range(10):
            if i % 3 == 0:
                line_width = 3
            else:
                line_width = 1
            # Vertical Line
            x = self.MARGIN + i * ((self.WIDTH - 2*self.MARGIN) / 9)
            self.canvas.create_line(x, self.MARGIN, x, self.HEIGHT - self.MARGIN, fill=colour, width=line_width)
        
            # Horizontal lines
            y = self.MARGIN + i * ((self.HEIGHT - 2*self.MARGIN) / 9)
            self.canvas.create_line(self.MARGIN, y, self.WIDTH - self.MARGIN, y, fill=colour, width=line_width)


    def _draw_puzzle(self, board):
        """
        Draws the puzzle values.
        """
        colour = "black"

        for i in range(9):
            for j in range(9):
                value = board[i][j]
                if value != 0:
                    if self.game.original_board[i][j] == 0:
                        FONT = ("garamond", 24)
                    else:
                        FONT = ("garamond", 24, "bold")
                    x = (self.MARGIN + j * ((self.WIDTH - 2 * self.MARGIN) / 9) + ((self.WIDTH - 2 * self.MARGIN) / 9) / 2)
                    y = (self.MARGIN + i * ((self.HEIGHT - 2 * self.MARGIN) / 9)
                    + ((self.WIDTH - 2 * self.MARGIN) / 9) / 2) 
                    self.canvas.create_text((x,y), text=str(int(value)), tag="numbers", font=FONT, fill=colour)


    def _update_puzzle(self, board):
        """
        Updates the puzzle board with board.
        """
        self.canvas.delete("numbers")
        self._draw_puzzle(board)

        # Activate undo button if moves greater than 1
        if self.game.move_count > 0:   
            self.undo_button.config(state="normal") 

        # Deactivate undo button if moves are 1
        if self.game.move_count == 0:
            self.undo_button.config(state="disabled")

        # Activate redo button if moves are same as the amount of boards.
        if self.game.move_count + 1 < len(self.game.board_history):
            self.redo_button.config(state="normal")

        # Deactivate redo button if moves are same as boards.
        if self.game.move_count + 1 == len(self.game.board_history):
            self.redo_button.config(state="disabled")

    
    def _left_click(self, event):
        """ Handles left click on canvas. """
        column, row = (int((event.x - self.MARGIN) / ((self.WIDTH - 2*self.MARGIN) / 9)), int((event.y - self.MARGIN) / ((self.HEIGHT - 2*self.MARGIN) / 9)))

        if  0 <= column < 9 and 0 <= row <9:
            self.canvas.focus_set()

            if self.cell_highlighted is not None:
                self.canvas.delete("selected")
                if (row == self.cell_highlighted[0] and column ==                   self.cell_highlighted[1]):
                        self.cell_highlighted = None
                        return

            # Bottom Left Corner
            x0, y0 = (self.MARGIN + column * ((self.WIDTH - 2*self.MARGIN) / 9), self.MARGIN + row * ((self.HEIGHT - 2*self.MARGIN) / 9) )

            # Bottom Right Corner
            x1, y1 = (self.MARGIN + (column + 1) * ((self.WIDTH - 2*self.MARGIN) / 9), self.MARGIN + (row + 1) * ((self.HEIGHT - 2*self.MARGIN) / 9) )
            
            self.canvas.create_rectangle(x0,y0,x1,y1, width="3", tag="selected")
            self.cell_highlighted = (row, column)                  

        print(self.game.board_history)
        print(self.game.move_count)


    def _key_press(self, event):
        """ A key press event. """

        if event.char in "123456789" and self.cell_highlighted is not None:
            print(event.char)
            if self.game.add_cell((self.cell_highlighted[0],   self.cell_highlighted[1]), event.char):
                self.canvas.delete("selected")
                self.cell_highlighted = None
                self._update_puzzle(self.game.board)


    def _backspace(self, event):
        """ Backspace press """
        if self.cell_highlighted is not None:
            if self.game.remove_cell((self.cell_highlighted[0],self.cell_highlighted[1])):
                self.canvas.delete("selected")
                self.cell_highlighted = None
                self._update_puzzle(self.game.board)


    def _undo(self):
        """ Method implementing undo button. """
        self.game.move_count  -= 1
        self.game.board = self.game.board_history[self.game.move_count]
        self._update_puzzle(self.game.board_history[self.game.move_count])


    def _redo(self):
        """ Method implementing the redo button. """
        self.game.move_count += 1
        self.game.board = self.game.board_history[self.game.move_count]
        self._update_puzzle(self.game.board_history[self.game.move_count])


    def _clear(self):
        """ Method implementing the clear board button. """
        if tk.messagebox.askyesno(title="Warning", message="Are you sure you want to clear?"):
            self.game.clear()
            self._update_puzzle(self.game.board)

    def _new_puzzle(self):
        """ Implentation of new puzzle button. """
        pass
            
