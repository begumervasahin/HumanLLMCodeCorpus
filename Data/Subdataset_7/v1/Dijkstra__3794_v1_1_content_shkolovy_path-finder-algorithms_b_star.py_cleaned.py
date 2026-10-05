from queue import PriorityQueue
from pprint import pprint
def fonk1():
    return [[0 for _ in range(10)] for _ in range(10)]
def fonk2(b8, b11, b1 = "m"):
    if b1 = = "m":
        return abs(b11[0] - b8[0]) + abs(b11[1] - b8[1])
    elif b1 = = "e":
        return ((b11[0] - b8[0]) ** 2 + (b11[1] - b8[1]) ** 2) ** 0.5
def fonk3(grid, x, y):
    b2 = []
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, b3 = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= b3 < len(grid[0]) and grid[nx][b3] == 0:
            b2.append((nx, b3))
    return b2
def fonk4(start, b11, b7):
    b4 = []
    b5 = b11
    while b5 != start:
        b4.append(b5)
        b5 = b7[b5]
    b4.append(start)
    b4.reverse()
    return b4
def fonk5(b4, grid):
    for x, y in b4:
        grid[x][y] = 1
def fonk6(grid, start, b11):
    b6 = PriorityQueue()
    b6.put((0, start))
    b7 = {start: None}
    while not b6.empty():
        b8 = b6.get()[1]
        if b8 = = b11:
            break
        b2 = fonk3(grid, b8[0], b8[1])
        for neighbor in b2:
            if neighbor not in b7:
                b9 = fonk2(neighbor, b11, b1="m")
                b6.put((b9, neighbor))
                b7[neighbor] = b8
    return b7
def fonk7():
    b10 = fonk1()
    start, b11 = (0, 0), (8, 8)
    b7 = fonk6(b10, start, b11)
    b4 = fonk4(start, b11, b7)
    fonk5(b4, b10)
    pprint(b10)
if b12 = = "__main__":
    fonk7()