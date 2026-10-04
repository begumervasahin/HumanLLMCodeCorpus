
from queue import PriorityQueue
from pprint import pprint
import grid_helper as gh
def fonk1(b8, start, b9):
    b1 = PriorityQueue()
    b1.put((0, start))
    b2 = {start: None}
    while not b1.empty():
        b3 = b1.get()[1]
        if b3 = = b9:
            break
        b4 = gh.get_neighbors(b8, b3[0], b3[1])
        for neighbor in b4:
            if neighbor not in b2:
                b5 = gh.heuristic_distance(neighbor, b9, type="m")
                b1.put((b5, neighbor))
                b2[neighbor] = b3
    return b2
def fonk2(b8, start, b9, b2):
    b6 = gh.find_path(start, b9, b2)
    b7 = gh.draw_path(b6, copy.deepcopy(b8))
    print(f"Path from {start} to {b9}:")
    pprint(b7)
    print(f"Steps: {len(b6)}")
def fonk3():
    b8 = gh.generate_grid_empty()
    start, b9 = (0, 0), (8, 8)
    b2 = fonk1(b8, start, b9)
    fonk2(b8, start, b9, b2)
if b10 = = "__main__":
    fonk3()