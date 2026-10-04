import random
import math
from tkinter import *
GRID_SIZE = 25
WINDOW_SIZE = 400
CELL_SIZE = WINDOW_SIZE / GRID_SIZE
maze = {}
visited = {}
walls = []
def add_walls(cell):
    if cell - GRID_SIZE >= 0:
        maze[(cell - GRID_SIZE, cell)] = 1
    if cell + GRID_SIZE < GRID_SIZE * GRID_SIZE:
        maze[(cell, cell + GRID_SIZE)] = 1
    if (cell + 1) % GRID_SIZE != 0:
        maze[(cell, cell + 1)] = 1
    if cell % GRID_SIZE != 0:
        maze[(cell - 1, cell)] = 1
for cell in range(GRID_SIZE * GRID_SIZE):
    visited[cell] = False
    add_walls(cell)
current_cell = 0
visited[current_cell] = True
walls += [[current_cell, neighbor] for neighbor in range(GRID_SIZE * GRID_SIZE) if (current_cell, neighbor) in maze.keys()]
while walls:
    random.shuffle(walls)
    wall = walls.pop()
    if visited[wall[0]] and not visited[wall[1]]:
        maze.pop((wall[0], wall[1]), None)
        maze.pop((wall[1], wall[0]), None)
        visited[wall[1]] = True
        walls += [[wall[1], neighbor] for neighbor in range(GRID_SIZE * GRID_SIZE) if (wall[1], neighbor) in maze.keys() or (neighbor, wall[1]) in maze.keys()]
    elif visited[wall[1]] and not visited[wall[0]]:
        maze.pop((wall[0], wall[1]), None)
        maze.pop((wall[1], wall[0]), None)
        visited[wall[0]] = True
        walls += [[wall[0], neighbor] for neighbor in range(GRID_SIZE * GRID_SIZE) if (wall[0], neighbor) in maze.keys() or (neighbor, wall[0]) in maze.keys()]
master = Tk()
canvas = Canvas(master, width=WINDOW_SIZE, height=WINDOW_SIZE)
canvas.pack()
canvas.create_rectangle(0, 0, WINDOW_SIZE, WINDOW_SIZE, fill="black")
canvas.create_rectangle(3, 3, WINDOW_SIZE - 3, WINDOW_SIZE - 3, fill="white")
def draw_wall(wall):
    wall_from = min(wall)
    wall_to = max(wall)
    wall_from_x = wall_from % GRID_SIZE
    wall_to_x = wall_to % GRID_SIZE
    wall_from_y = math.floor(min(wall_from / GRID_SIZE, wall_to / GRID_SIZE))
    wall_to_y = math.floor(max(wall_to / GRID_SIZE, wall_from / GRID_SIZE))
    if wall_from_x == wall_to_x:
        rect_x_from = wall_from_x * CELL_SIZE
        rect_x_to = wall_from_x * CELL_SIZE + CELL_SIZE
        rect_y_from = wall_from_y * CELL_SIZE + CELL_SIZE - 1
        rect_y_to = wall_from_y * CELL_SIZE + CELL_SIZE + 1
        canvas.create_rectangle(rect_x_from, rect_y_from, rect_x_to, rect_y_to, fill="black")
    if wall_from_y == wall_to_y:
        rect_y_from = wall_from_y * CELL_SIZE
        rect_y_to = wall_from_y * CELL_SIZE + CELL_SIZE
        rect_x_from = wall_from_x * CELL_SIZE + CELL_SIZE - 1
        rect_x_to = wall_from_x * CELL_SIZE + CELL_SIZE + 1
        canvas.create_rectangle(rect_x_from, rect_y_from, rect_x_to, rect_y_to, fill="black")
for wall in maze:
    draw_wall(wall)
canvas.create_rectangle(0, 4, 3, CELL_SIZE + 3, fill="yellow", outline="white")
canvas.create_rectangle(WINDOW_SIZE - 4, WINDOW_SIZE - CELL_SIZE, WINDOW_SIZE, WINDOW_SIZE - 4, fill="green", outline="white")
mainloop()