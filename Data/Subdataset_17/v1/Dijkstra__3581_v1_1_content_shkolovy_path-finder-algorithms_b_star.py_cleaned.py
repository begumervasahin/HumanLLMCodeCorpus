
from queue import PriorityQueue
from pprint import pprint
import grid_helper as gh
def find_path_greedy(grid, start, end):
    pq = PriorityQueue()
    pq.put((0, start))
    came_from = {start: None}
    while not pq.empty():
        current_pos = pq.get()[1]
        if current_pos == end:
            break
        neighbors = gh.get_neighbors(grid, current_pos[0], current_pos[1])
        for neighbor in neighbors:
            if neighbor not in came_from:
                priority = gh.heuristic_distance(neighbor, end, type="m")
                pq.put((priority, neighbor))
                came_from[neighbor] = current_pos
    return came_from
def display_path(grid, start, end, came_from):
    path = gh.find_path(start, end, came_from)
    grid_with_path = gh.draw_path(path, copy.deepcopy(grid))
    print(f"Path from {start} to {end}:")
    pprint(grid_with_path)
    print(f"Steps: {len(path)}")
def initialize():
    initial_grid = gh.generate_grid_empty()
    start, end = (0, 0), (8, 8)
    came_from = find_path_greedy(initial_grid, start, end)
    display_path(initial_grid, start, end, came_from)
if __name__ == "__main__":
    initialize()