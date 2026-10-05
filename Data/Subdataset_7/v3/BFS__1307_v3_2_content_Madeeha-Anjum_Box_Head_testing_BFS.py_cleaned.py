import collections
def fonk1(b8, start):
    b1 = collections.deque([[start]])
    b2 = set([start])
    while b1:
        b3 = b1.popleft()
        x, b4 = b3[-1]
        if b8[b4][x] == goal:
            return b3
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            x2, b5 = x + dx, b4 + dy
            if 0 <= x2 < columns and 0 <= b5 < rows and b8[b5][x2] != wall and (x2, b5) not in b2:
                b1.append(b3 + [(x2, b5)])
                b2.add((x2, b5))
WALL, CLEAR, b6 = "
COLUMNS, b7 = 10, 5
b8 = [
    "..........",
    "...
    "..
    ".....
    ".........."
]
b9 = (0, 0)
print(fonk1(b8, b9))
