2. Repository: Madeeha-Anjum/Box_Head
   File: testing_BFS.py
   URL: https:
   Code Content:
import collections
def bfs(grid, start):
    print(type(start))
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if grid[y][x] == goal:
            return path
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < collombs and 0 <= y2 < rows  and grid[y2][x2] != wall and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
wall, clear, goal = "
collombs, rows = 10, 5
grid = ["..........",
        "...
        "..
        ".....
        ".........."]
print("length of test grid",len(grid))
print(grid[2][5])
print(grid[2][4])
print(grid[3][4])
print(grid[4][4])
print(grid[4][5])
   README Content:
Pygame on python3
NOT FINISHED!!!
YOUTUBE:
https:
How to Run the game using the terminal:
python3 main.py
Description:
move: arrow keys
shoot: space
start: UP ARROW
This game is a modified version of  "Box Head"
The objective of the game is to kill as many zombies as possible. When the games loads,
the start/end screen is displayed. Press UP KEY to begin. To control the player, use the
arrow keys to move around. Press the space bar to shoot. At the top of the screen, there
is a health bar that keeps track of the player's health, and a score value. The zombie is
killed when hit with a bullet. More will respawn The zombies are randomly created ever 7
seconds For each zombie killed, the player is awarded with 10 points. The game ends when
the player loses all of their health.
