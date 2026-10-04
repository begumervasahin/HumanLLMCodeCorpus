from pprint import pprint
from collections import deque
import copy
import grid_helper as gh
def fonk1(grid, b1 = (0, 0)):
    b2 = deque([b1])
    b3 = {b1: None}
    while b2:
        b4 = b2.popleft()
        b5 = gh.get_neighbors(grid, b4[0], b4[1])
        for neighbor in b5:
            if neighbor not in b3:
                b2.append(neighbor)
                b3[neighbor] = b4
    return b3
def fonk2(grid, b9, end_pos, b10):
    b6 = gh.find_path(b9, end_pos, b10)
    b7 = gh.draw_path(b6, copy.deepcopy(grid))
    print(f"Path to {end_pos}:")
    pprint(b7)
    print(f"Steps: {len(b6)}")
def fonk3():
    b8 = gh.generate_grid_obstacle()
    b9 = (3, 0)
    b10 = fonk1(b8, b9)
    fonk2(b8, b9, (8, 8), b10)
    fonk2(b8, b9, (4, 7), b10)
if b11 = = "__main__":
    fonk3()