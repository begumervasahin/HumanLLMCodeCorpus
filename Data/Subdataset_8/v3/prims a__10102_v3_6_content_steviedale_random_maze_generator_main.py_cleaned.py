
from maze import Maze
from graphics import BoardDisplay
from time import sleep
MAZE_WIDTH = 20
PATH_WIDTH = 25
class Maze:
    def __init__(self, width):
        self.width = width
    def complete_trace(self):
        pass
class BoardDisplay:
    def __init__(self, num_rows, num_columns, width):
        self.num_rows = num_rows
        self.num_columns = num_columns
        self.width = width
    def start(self, trace_function):
        pass
board_display = BoardDisplay(num_rows=MAZE_WIDTH, num_columns=MAZE_WIDTH, width=PATH_WIDTH)
maze = Maze(width=MAZE_WIDTH)
board_display.start(trace_function=maze.complete_trace)