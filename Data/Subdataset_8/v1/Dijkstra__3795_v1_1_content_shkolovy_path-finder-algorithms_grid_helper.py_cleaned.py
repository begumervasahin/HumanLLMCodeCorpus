import math
START_COL = "S"
END_COL = "E"
VISITED_COL = "x"
OBSTACLE_COL = "O"
PATH_COL = "@"
def generate_grid_empty():
    return [["." for _ in range(9)] for _ in range(9)]
def heuristic_distance(pos, end_pos, type="e"):
    dx = abs(pos[0] - end_pos[0])
    dy = abs(pos[1] - end_pos[1])
    if type == "m":
        return dx + dy
    return math.sqrt(dx * dx + dy * dy)
def find_path(start, end, came_from):
    path = [end]
    current = end
    while current != start:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path
def get_cost(grid, pos):
    col_val = grid[pos[0]][pos[1]]
    return int(col_val) if col_val.isdigit() else 1
def get_neighbors(grid, row, col):
    height = len(grid)
    width = len(grid[0])
    neighbors = [(row + 1, col), (row, col - 1), (row - 1, col), (row, col + 1)]
    if (row + col) % 2 == 0:
        neighbors.reverse()
    neighbors = filter(lambda t: (0 <= t[0] < height and 0 <= t[1] < width), neighbors)
    neighbors = filter(lambda t: (grid[t[0]][t[1]] != OBSTACLE_COL), neighbors)
    return neighbors
def draw_path(path, grid):
    for row, col in path:
        grid[row][col] = PATH_COL
    start_pos = path[0]
    end_pos = path[-1]
    grid[start_pos[0]][start_pos[1]] = START_COL
    grid[end_pos[0]][end_pos[1]] = END_COL
    return grid
initial_grid = generate_grid_empty()
start_pos = (0, 0)
end_pos = (8, 8)
came_from = {(8, 8): (7, 8), (7, 8): (7, 7), (7, 7): (6, 7), (6, 7): (5, 7), (5, 7): (4, 7), (4, 7): (4, 6),
             (4, 6): (4, 5), (4, 5): (4, 4), (4, 4): (3, 4), (3, 4): (2, 4), (2, 4): (1, 4), (1, 4): (0, 4),
             (0, 4): (0, 3), (0, 3): (0, 2), (0, 2): (0, 1), (0, 1): (0, 0)}
path = find_path(start_pos, end_pos, came_from)
grid_with_path = draw_path(path, initial_grid)
for row in grid_with_path:
    print(" ".join(row))