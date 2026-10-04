import collections
def bfs(grid, start):
    queue = collections.deque([[start]])
    seen = set([start])
    rows, columns = len(grid), len(grid[0])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if grid[y][x] == goal:
            return path
        for x2, y2 in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if 0 <= x2 < columns and 0 <= y2 < rows and grid[y2][x2] != wall and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
    return None
wall, clear, goal = "
grid = [
    "..........",
    "...
    "..
    ".....
    ".........."
]
grid = [list(row) for row in grid]
start_position = (0, 0)
path = bfs(grid, start_position)
if path:
    print("Path to goal:", path)
else:
    print("No path found to the goal.")
