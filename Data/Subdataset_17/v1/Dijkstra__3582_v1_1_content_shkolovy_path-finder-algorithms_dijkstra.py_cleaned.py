
from queue import PriorityQueue
from pprint import pprint
import grid_helper as gh
def find_path_dijkstra(grid, start, end):
    priority_queue = PriorityQueue()
    priority_queue.put((0, start))
    came_from = {start: None}
    costs = {start: 0}
    while not priority_queue.empty():
        current_position = priority_queue.get()[1]
        if current_position == end:
            break
        neighbors = gh.get_neighbors(grid, current_position[0], current_position[1])
        for neighbor in neighbors:
            new_cost = costs[current_position] + gh.get_cost(grid, neighbor)
            if neighbor not in costs or new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                priority_queue.put((new_cost, neighbor))
                came_from[neighbor] = current_position
    return came_from
def display_path(grid, start, end, came_from):
    path = gh.find_path(start, end, came_from)
    grid_with_path = gh.draw_path(path, copy.deepcopy(grid))
    print(f"Path from {start} to {end}:")
    pprint(grid_with_path)
    print(f"Steps: {len(path)}")
def initialize():
    initial_grid = gh.generate_grid_weighted()
    start, end = (4, 0), (4, 6)
    came_from = find_path_dijkstra(initial_grid, start, end)
    display_path(initial_grid, start, end, came_from)
if __name__ == "__main__":
    initialize()