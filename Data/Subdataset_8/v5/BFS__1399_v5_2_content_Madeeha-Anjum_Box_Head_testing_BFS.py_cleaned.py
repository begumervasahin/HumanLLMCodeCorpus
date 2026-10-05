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
            nx, ny = x + dx, y + dy
            if 0 <= nx < columns and 0 <= ny < rows and grid[ny][nx] != wall and (nx, ny) not in seen:
                queue.append(path + [(nx, ny)])
                seen.add((nx, ny))
wall, clear, goal = "
columns, rows = 10, 5
grid = ["..........",
        "...
        "..
        ".....
        ".........."]
print("Length of test grid:", len(grid))
print("Sample grid values:")
print(grid[2][5])
print(grid[2][4])
print(grid[3][4])
print(grid[4][4])
print(grid[4][5])
print("\nExplanation:")
print("- The grid represents a layout where '.' denotes clear space, '
print("- The BFS algorithm searches for a path from the start position to the goal, avoiding walls.")
print("- Grid boundaries and wall positions are checked to ensure valid moves.")