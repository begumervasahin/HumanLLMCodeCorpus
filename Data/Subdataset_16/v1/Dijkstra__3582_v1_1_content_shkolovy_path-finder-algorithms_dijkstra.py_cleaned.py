
from queue import PriorityQueue
from pprint import pprint
import grid_helper as gh
def fonk1(grid, start, b10):
    b1 = PriorityQueue()
    b1.put((0, start))
    b2 = {start: None}
    b3 = {start: 0}
    while not b1.empty():
        b4 = b1.get()[1]
        if b4 = = b10:
            break
        b5 = gh.get_neighbors(grid, b4[0], b4[1])
        for neighbor in b5:
            b6 = b3[b4] + gh.get_cost(grid, neighbor)
            if neighbor not in b3 or b6 < b3[neighbor]:
                b3[neighbor] = b6
                b1.put((b6, neighbor))
                b2[neighbor] = b4
    return b2
def fonk2(grid, start, b10, b2):
    b7 = gh.find_path(start, b10, b2)
    b8 = gh.draw_path(b7, copy.deepcopy(grid))
    print(f"Path from {start} to {b10}:")
    pprint(b8)
    print(f"Steps: {len(b7)}")
def fonk3():
    b9 = gh.generate_grid_weighted()
    start, b10 = (4, 0), (4, 6)
    b2 = fonk1(b9, start, b10)
    fonk2(b9, start, b10, b2)
if b11 = = "__main__":
    fonk3()