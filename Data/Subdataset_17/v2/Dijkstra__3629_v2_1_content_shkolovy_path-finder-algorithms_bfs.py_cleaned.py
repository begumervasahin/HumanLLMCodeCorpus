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
def initialize():
    grid = gh.generate_grid_obstacle()
    start_position = (3, 0)
    directions = scan_grid(grid, start_position)
    path_to_88 = gh.find_path(start_position, (8, 8), directions)
    grid_with_path_88 = gh.draw_path(path_to_88, copy.deepcopy(grid))
    print("Path to (8, 8):")
    pprint(grid_with_path_88)
    print(f"Steps: {len(path_to_88)}")
    path_to_47 = gh.find_path(start_position, (4, 7), directions)
    grid_with_path_47 = gh.draw_path(path_to_47, copy.deepcopy(grid))
    print("Path to (4, 7):")
    pprint(grid_with_path_47)
    print(f"Steps: {len(path_to_47)}")
if __name__ == "__main__":
    initialize()