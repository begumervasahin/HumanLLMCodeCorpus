import collections
def bfs(grid, start):
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if grid[y][x] == goal:
            return path
        for x2, y2 in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            if 0 <= x2 < collombs and 0 <= y2 < rows and grid[y2][x2] != wall and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
wall, clear, goal = "
collombs, rows = 10, 5
grid = ["..........",
        "...
        "..
        ".....
        ".........."]
print("length of test grid:", len(grid))
print(grid[2][5])
print(grid[2][4])
print(grid[3][4])
print(grid[4][4])
print(grid[4][5])
