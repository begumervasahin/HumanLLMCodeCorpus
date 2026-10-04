
from queue import PriorityQueue
import grid_helper as gh
from pprint import pprint
def fonk1(grid, start, b8):
    b1 = PriorityQueue()
    b1.put((0, start))
    b2 = {start: None}
    b3 = {start: 0}
    while not b1.empty():
        b4 = b1.get()[1]
        if b4 = = b8:
            break
        b5 = gh.get_neighbors(grid, b4[0], b4[1])
        for neighbor in b5:
            b6 = b3[b4] + gh.get_cost(grid, neighbor)
            if neighbor not in b3 or b6 < b3[neighbor]:
                b3[neighbor] = b6
                b1.put((b6, neighbor))
                b2[neighbor] = b4
    return b2
def fonk2():
    b7 = gh.generate_grid_weighted()
    start, b8 = (4, 0), (4, 6)
    b2 = fonk1(b7, start, b8)
    b9 = gh.find_path(start, b8, b2)
    gh.draw_path(b9, b7)
    pprint(b7)
if b10 = = "__main__":
    fonk2()