import random
import math
from tkinter import *
SIZE = 25
WINDOW_SIZE = 400
WALL_SIZE = WINDOW_SIZE / SIZE
maze = {}
visited = {i: False for i in range(SIZE * SIZE)}
walls = []
for i in range(SIZE * SIZE):
    if i - SIZE >= 0:
        maze[(i - SIZE, i)] = 1
    if i + SIZE < SIZE * SIZE - SIZE:
        maze[(i, i + SIZE)] = 1
    if not (i + 1) % SIZE == 0:
        maze[(i, i + 1)] = 1
    if not i % SIZE == 0:
        maze[(i - 1, i)] = 1
cell = 0
visited[0] = True
walls += [[0, x] for x in range(SIZE * SIZE) if (0, x) in maze]
while walls:
    random.shuffle(walls)
    wall = walls.pop()
    if visited[wall[0]] and not visited[wall[1]]:
        maze.pop((wall[0], wall[1]), None)
        maze.pop((wall[1], wall[0]), None)
        visited[wall[1]] = True
        walls += [[wall[1], x] for x in range(SIZE * SIZE) if (wall[1], x) in maze or (x, wall[1]) in maze]
    elif visited[wall[1]] and not visited[wall[0]]:
        maze.pop((wall[0], wall[1]), None)
        maze.pop((wall[1], wall[0]), None)
        visited[wall[0]] = True
        walls += [[wall[0], x] for x in range(SIZE * SIZE) if (wall[0], x) in maze or (x, wall[0]) in maze]
master = Tk()
canvas = Canvas(master, width=WINDOW_SIZE, height=WINDOW_SIZE)
canvas.pack()
canvas.create_rectangle(0, 0, WINDOW_SIZE, WINDOW_SIZE, fill="black")
canvas.create_rectangle(3, 3, WINDOW_SIZE - 3, WINDOW_SIZE - 3, fill="white")
for wall in maze:
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
canvas.create_rectangle(0, 4, 3, WALL_SIZE + 3, fill="yellow", outline="white")
canvas.create_rectangle(WINDOW_SIZE - 4, WINDOW_SIZE - WALL_SIZE, WINDOW_SIZE, WINDOW_SIZE - 4, fill="green", outline="white")
mainloop()