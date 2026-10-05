from queue import PriorityQueue
import grid_helper as gh
from pprint import pprint
def fonk1(grid, start, b7):
    b1 = PriorityQueue()
    b1.put((0, start))
    b2 = {start: None}
    while not b1.empty():
        b3 = b1.get()[1]
        if b3 = = b7:
            break
        b4 = gh.get_neighbors(grid, b3[0], b3[1])
        for neighbor in b4:
            if neighbor not in b2:
                b5 = gh.heuristic_distance(neighbor, b7, type="manhattan")
                b1.put((b5, neighbor))
                b2[neighbor] = b3
    return b2
def fonk2():
    b6 = gh.generate_grid_empty()
    start, b7 = (0, 0), (8, 8)
    b2 = fonk1(b6, start, b7)
    b8 = gh.find_path(start, b7, b2)
    gh.draw_path(b8, b6)
    pprint(b6)
if b9 = = "__main__":
    fonk2()