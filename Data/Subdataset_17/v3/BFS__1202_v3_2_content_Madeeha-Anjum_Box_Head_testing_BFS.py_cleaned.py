import collections
def bfs(grid, start):
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if grid[y][x] == GOAL:
            return path
        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= x2 < COLUMNS and 0 <= y2 < ROWS and grid[y2][x2] != WALL and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
    return None
WALL = "
CLEAR = "."
GOAL = "*"
COLUMNS, ROWS = 10, 5
grid = [
    "..........",
    "...
    "..
    ".....
    ".........."
]
start = (0, 0)
path = bfs(grid, start)
if path:
    print("Path to goal:", path)
else:
    print("No path found")