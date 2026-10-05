import collections
def bfs(grid, start):
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if grid[y][x] == goal:
            return path
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            x2, y2 = x + dx, y + dy
            if 0 <= x2 < columns and 0 <= y2 < rows and grid[y2][x2] != wall and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
WALL, CLEAR, GOAL = "
COLUMNS, ROWS = 10, 5
grid = [
    "..........",
    "...
    "..
    ".....
    ".........."
]
start_position = (0, 0)
print(bfs(grid, start_position))
