
from maze import Maze
from graphics import BoardDisplay
from time import sleep
maze_width = 20
path_width = 25
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
disp = BoardDisplay(num_rows=maze_width, num_columns=maze_width, width=path_width)
maze = Maze(maze_width)
disp.start(maze.complete_trace)