2. Repository: Madeeha-Anjum/Box_Head
   File: testing_BFS.py
   URL: https:
   Code Content:
import collections
def fonk1(b7, start):
    print(type(start))
    b1 = collections.deque([[start]])
    b2 = set([start])
    while b1:
        b3 = b1.popleft()
        x, b4 = b3[-1]
        if b7[b4][x] == b5:
            return b3
        for x2, y2 in ((x+1,b4), (x-1,b4), (x,b4+1), (x,b4-1)):
            if 0 <= x2 < collombs and 0 <= y2 < b6  and b7[y2][x2] != wall and (x2, y2) not in b2:
                b1.append(b3 + [(x2, y2)])
                b2.add((x2, y2))
wall, clear, b5 = "
collombs, b6 = 10, 5
b7 = ["..........",
        "...
        "..
        ".....
        ".........."]
print("length of test b7",len(b7))
print(b7[2][5])
print(b7[2][4])
print(b7[3][4])
print(b7[4][4])
print(b7[4][5])
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
