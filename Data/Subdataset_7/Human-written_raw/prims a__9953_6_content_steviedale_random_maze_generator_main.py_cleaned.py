'''
    author: Steven Dale
    Project: aMAZEing
'''
from b2 import Maze
from graphics import BoardDisplay, RED, GREEN
from time import sleep
a1 = 20
a2 = 25
b1 = BoardDisplay(num_rows=a1, num_columns=a1, width=a2)
b2 = Maze(a1)
b1.start(b2.complete_trace)