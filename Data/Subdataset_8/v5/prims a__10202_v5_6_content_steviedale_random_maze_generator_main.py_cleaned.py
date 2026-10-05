
from maze import Maze
from graphics import BoardDisplay, RED, GREEN
from time import sleep
maze_width = 20
path_width = 25
board_display = BoardDisplay(num_rows=maze_width, num_columns=maze_width, width=path_width)
maze = Maze(maze_width)
board_display.start(maze.complete_trace)