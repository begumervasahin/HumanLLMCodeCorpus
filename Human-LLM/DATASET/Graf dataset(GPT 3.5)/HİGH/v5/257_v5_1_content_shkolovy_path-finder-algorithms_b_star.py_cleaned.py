from queue import PriorityQueue
import grid_helper as gh
from pprint import pprint
def fonk1(grid_map, start, b8):
    b1 = PriorityQueue()
    b1.put((0, start))
    b2 = {start: None}
    while not b1.empty():
        b3 = b1.get()[1]
        if b3 = = b8:
            break
        b4 = gh.get_neighbors(grid_map, b3[0], b3[1])
        for neighbor in b4:
            if neighbor not in b2:
                b5 = gh.heuristic_distance(neighbor, b8, type="manhattan")
                b1.put((b5, neighbor))
                b2[neighbor] = b3
    return b2
if b6 = = "__main__":
    b7 = gh.generate_grid_empty()
    start, b8 = (0, 0), (8, 8)
    b2 = fonk1(b7, start, b8)
    b9 = gh.find_path(start, b8, b2)
    gh.draw_path(b9, b7)
    pprint(b7)