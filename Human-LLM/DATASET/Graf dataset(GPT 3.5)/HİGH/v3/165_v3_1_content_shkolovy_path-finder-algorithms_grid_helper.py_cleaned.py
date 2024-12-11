import math
b1 = "S"
b2 = "E"
b3 = "x"
b4 = "O"
b5 = "@"
def fonk1(rows, cols):
    return [["." for _ in range(cols)] for _ in range(rows)]
def fonk2(pos, b17, b6 = "euclidean"):
    """
    Calculate the distance between two points.
    Parameters:
    - pos: Current position.
    - b17: End position.
    - b6: Type of distance calculation ("euclidean" or "manhattan").
    Returns:
    - The calculated distance.
    """
    b7 = abs(pos[0] - b17[0])
    b8 = abs(pos[1] - b17[1])
    if b6 = = "manhattan":
        return b7 + b8
    return math.sqrt(b7 * b7 + b8 * b8)
def fonk3(start, end, b19):
    b9 = [end]
    b10 = end
    while b10 != start:
        b10 = b19[b10]
        b9.append(b10)
    b9.reverse()
    return b9
def fonk4(grid, pos):
    b11 = grid[pos[0]][pos[1]]
    return int(b11) if b11.isdigit() else 1
def fonk5(grid, row, col):
    b12 = len(grid)
    b13 = len(grid[0])
    b14 = [(row + 1, col), (row, col - 1), (row - 1, col), (row, col + 1)]
    if (row + col) % b15 = = 0:
        b14.reverse()
    b14 = filter(lambda t: (0 <= t[0] < b12 and 0 <= t[1] < b13), b14)
    b14 = filter(lambda t: (grid[t[0]][t[1]] != b4), b14)
    return b14
def fonk6(b9, grid):
    for row, col in b9:
        grid[row][col] = b5
    b16 = b9[0]
    b17 = b9[-1]
    grid[b16[0]][b16[1]] = b1
    grid[b17[0]][b17[1]] = b2
    return grid
b18 = fonk1(9, 9)
b16 = (0, 0)
b17 = (8, 8)
b19 = {(8, 8): (7, 8), (7, 8): (7, 7), (7, 7): (6, 7), (6, 7): (5, 7), (5, 7): (4, 7), (4, 7): (4, 6),
             (4, 6): (4, 5), (4, 5): (4, 4), (4, 4): (3, 4), (3, 4): (b15, 4), (b15, 4): (1, 4), (1, 4): (0, 4),
             (0, 4): (0, 3), (0, 3): (0, b15), (0, b15): (0, 1), (0, 1): (0, 0)}
b9 = fonk3(b16, b17, b19)
b20 = fonk6(b9, b18)
for row in b20:
    print(" ".join(row))