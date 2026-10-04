
import random
import math
from tkinter import *
SIZE = 25
WINDOW_SIZE = 400
WALL_SIZE = WINDOW_SIZE / SIZE
maze = {}
visited = {i: False for i in range(SIZE * SIZE)}
walls = []
def initialize_maze():
    for i in range(SIZE * SIZE):
        if i - SIZE >= 0:
            maze[(i - SIZE, i)] = 1
        if i + SIZE < SIZE * SIZE:
            maze[(i, i + SIZE)] = 1
        if (i + 1) % SIZE != 0:
            maze[(i, i + 1)] = 1
        if i % SIZE != 0:
            maze[(i - 1, i)] = 1
def start_maze():
    cell = 0
    visited[0] = True
    walls.extend([[0, x] for x in range(SIZE * SIZE) if (0, x) in maze])
def generate_maze():
    while walls:
        random.shuffle(walls)
        wall = walls.pop()
        if visited[wall[0]] and not visited[wall[1]]:
            remove_wall(wall)
            visited[wall[1]] = True
            extend_walls(wall[1])
        elif visited[wall[1]] and not visited[wall[0]]:
            remove_wall(wall)
            visited[wall[0]] = True
            extend_walls(wall[0])
def remove_wall(wall):
    maze.pop((wall[0], wall[1]), None)
    maze.pop((wall[1], wall[0]), None)
def extend_walls(cell):
    walls.extend([[cell, x] for x in range(SIZE * SIZE) if (cell, x) in maze or (x, cell) in maze])
def create_window():
    master = Tk()
    canvas = Canvas(master, width=WINDOW_SIZE, height=WINDOW_SIZE)
    canvas.pack()
    draw_maze(canvas)
    draw_entry_exit_points(canvas)
    mainloop()
def draw_maze(canvas):
    canvas.create_rectangle(0, 0, WINDOW_SIZE, WINDOW_SIZE, fill="black")
    canvas.create_rectangle(3, 3, WINDOW_SIZE - 3, WINDOW_SIZE - 3, fill="white")
    for wall in maze:
        draw_wall(canvas, wall)
def draw_wall(canvas, wall):
    wall_from = min(wall)
    wall_to = max(wall)
    wall_from_x = wall_from % SIZE
    wall_to_x = wall_to % SIZE
    wall_from_y = math.floor(min(wall_from / SIZE, wall_to / SIZE))
    wall_to_y = math.floor(max(wall_to / SIZE, wall_from / SIZE))
    if wall_from_x == wall_to_x:
        rect_x_from = wall_from_x * WALL_SIZE
        rect_x_to = wall_from_x * WALL_SIZE + WALL_SIZE
        rect_y_from = wall_from_y * WALL_SIZE + WALL_SIZE - 1
        rect_y_to = wall_from_y * WALL_SIZE + WALL_SIZE + 1
        canvas.create_rectangle(rect_x_from, rect_y_from, rect_x_to, rect_y_to, fill="black")
    elif wall_from_y == wall_to_y:
        rect_y_from = wall_from_y * WALL_SIZE
        rect_y_to = wall_from_y * WALL_SIZE + WALL_SIZE
        rect_x_from = wall_from_x * WALL_SIZE + WALL_SIZE - 1
        rect_x_to = wall_from_x * WALL_SIZE + WALL_SIZE + 1
        canvas.create_rectangle(rect_x_from, rect_y_from, rect_x_to, rect_y_to, fill="black")
def draw_entry_exit_points(canvas):
    canvas.create_rectangle(0, 4, 3, WALL_SIZE + 3, fill="yellow", outline="white")
    canvas.create_rectangle(WINDOW_SIZE - 4, WINDOW_SIZE - WALL_SIZE, WINDOW_SIZE, WINDOW_SIZE - 4, fill="green", outline="white")
if __name__ == "__main__":
    initialize_maze()
    start_maze()
    generate_maze()
    create_window()