import collections
def fonk1(b7, start):
    b1 = collections.deque([[start]])
    b2 = set([start])
    rows, b3 = len(b7), len(b7[0])
    while b1:
        b4 = b1.popleft()
        x, b5 = b4[-1]
        if b7[b5][x] == b6:
            return b4
        for x2, y2 in [(x + 1, b5), (x - 1, b5), (x, b5 + 1), (x, b5 - 1)]:
            if 0 <= x2 < b3 and 0 <= y2 < rows and b7[y2][x2] != wall and (x2, y2) not in b2:
                b1.append(b4 + [(x2, y2)])
                b2.add((x2, y2))
    return None
wall, clear, b6 = "
b7 = [
    "..........",
    "...
    "..
    ".....
    ".........."
]
b7 = [list(row) for row in b7]
b8 = (0, 0)
b4 = fonk1(b7, b8)
if b4:
    print("Path to b6:", b4)
else:
    print("No b4 found to the b6.")
