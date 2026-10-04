from pprint import pprint
from collections import deque
import copy
import grid_helper as gh
def fonk1(grid, b1 = (0, 0)):
    b2 = deque()
    b2.append(b1)
    b3 = {b1: None}
    while len(b2) > 0:
        b4 = b2.popleft()
        b5 = gh.get_neighbors(grid, b4[0], b4[1])
        for neighbor in b5:
            if neighbor not in b3:
                b2.append(neighbor)
                b3[neighbor] = b4
    return b3
def fonk2():
    b6 = gh.generate_grid_obstacle()
    b7 = (3, 0)
    b8 = fonk1(b6, b7)
    b9 = gh.find_path(b7, (8, 8), b8)
    b10 = gh.draw_path(b9, copy.deepcopy(b6))
    pprint(b10)
    print(f"steps: {len(b9)}")
    b11 = gh.find_path(b7, (4, 7), b8)
    b12 = gh.draw_path(b11, copy.deepcopy(b6))
    pprint(b12)
    print(f"steps: {len(b11)}")
if b13 = = "__main__":
    fonk2()