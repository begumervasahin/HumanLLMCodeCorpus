from queue import PriorityQueue
from pprint import pprint
def fonk1(b1 = 10):
    return [[0 for _ in range(b1)] for _ in range(b1)]
def fonk2(b9, b12, b2 = "manhattan"):
    if b2 = = "manhattan":
        return abs(b12[0] - b9[0]) + abs(b12[1] - b9[1])
    elif b2 = = "euclidean":
        return ((b12[0] - b9[0]) ** 2 + (b12[1] - b9[1]) ** 2) ** 0.5
def fonk3(grid, x, y):
    b3 = []
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, b4 = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= b4 < len(grid[0]) and grid[nx][b4] == 0:
            b3.append((nx, b4))
    return b3
def fonk4(start, b12, b8):
    b5 = []
    b6 = b12
    while b6 != start:
        b5.append(b6)
        b6 = b8[b6]
    b5.append(start)
    b5.reverse()
    return b5
def fonk5(b5, grid):
    for x, y in b5:
        grid[x][y] = 1
def fonk6(grid, start, b12):
    b7 = PriorityQueue()
    b7.put((0, start))
    b8 = {start: None}
    while not b7.empty():
        b9 = b7.get()[1]
        if b9 = = b12:
            break
        b3 = fonk3(grid, b9[0], b9[1])
        for neighbor in b3:
            if neighbor not in b8:
                b10 = fonk2(neighbor, b12, b2="manhattan")
                b7.put((b10, neighbor))
                b8[neighbor] = b9
    return b8
def fonk7():
    b11 = fonk1()
    start, b12 = (0, 0), (8, 8)
    b8 = fonk6(b11, start, b12)
    b5 = fonk4(start, b12, b8)
    fonk5(b5, b11)
    pprint(b11)
if b13 = = "__main__":
    fonk7()