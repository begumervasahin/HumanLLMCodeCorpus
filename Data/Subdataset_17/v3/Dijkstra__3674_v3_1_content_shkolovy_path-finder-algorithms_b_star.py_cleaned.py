
from queue import PriorityQueue
from pprint import pprint
import grid_helper as gh
def find_path_greedy(grid, start, end):
    priority_queue = PriorityQueue()
    priority_queue.put((0, start))
    came_from = {start: None}
    while not priority_queue.empty():
        current = priority_queue.get()[1]
        if current == end:
            break
        neighbors = gh.get_neighbors(grid, current[0], current[1])
        for neighbor in neighbors:
            if neighbor not in came_from:
                priority = gh.heuristic_distance(neighbor, end, type="m")
                priority_queue.put((priority, neighbor))
                came_from[neighbor] = current
    return came_from
def display_path(grid, start, end, came_from):
    path = gh.find_path(start, end, came_from)
    grid_with_path = gh.draw_path(path, copy.deepcopy(grid))
    print(f"Path from {start} to {end}:")
    pprint(grid_with_path)
    print(f"Steps: {len(path)}")
def initialize():
    grid = gh.generate_grid_empty()
    start, end = (0, 0), (8, 8)
    came_from = find_path_greedy(grid, start, end)
    display_path(grid, start, end, came_from)
if __name__ == "__main__":
    initialize()