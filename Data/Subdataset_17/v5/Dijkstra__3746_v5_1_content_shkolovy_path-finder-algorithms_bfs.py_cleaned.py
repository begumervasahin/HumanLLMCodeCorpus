from pprint import pprint
from collections import deque
import copy
import grid_helper as gh
def scan_grid(grid, start=(0, 0)):
    queue = deque([start])
    came_from = {start: None}
    while queue:
        current = queue.popleft()
        neighbors = gh.get_neighbors(grid, current[0], current[1])
        for neighbor in neighbors:
            if neighbor not in came_from:
                queue.append(neighbor)
                came_from[neighbor] = current
    return came_from
def display_path(grid, start_pos, end_pos, directions):
    path = gh.find_path(start_pos, end_pos, directions)
    grid_with_path = gh.draw_path(path, copy.deepcopy(grid))
    print(f"Path to {end_pos}:")
    pprint(grid_with_path)
    print(f"Steps: {len(path)}")
def initialize():
    initial_grid = gh.generate_grid_obstacle()
    start_pos = (3, 0)
    directions = scan_grid(initial_grid, start_pos)
    display_path(initial_grid, start_pos, (8, 8), directions)
    display_path(initial_grid, start_pos, (4, 7), directions)
if __name__ == "__main__":
    initialize()