import collections
def fonk1(b9, b10):
    b1 = collections.deque([[b10]])
    b2 = set([b10])
    while b1:
        b3 = b1.popleft()
        x, b4 = b3[-1]
        if b9[b4][x] == b7:
            return b3
        for x2, y2 in ((x + 1, b4), (x - 1, b4), (x, b4 + 1), (x, b4 - 1)):
            if 0 <= x2 < COLUMNS and 0 <= y2 < b8 and b9[y2][x2] != b5 and (x2, y2) not in b2:
                b1.append(b3 + [(x2, y2)])
                b2.add((x2, y2))
    return None
b5 = "
b6 = "."
b7 = "*"
COLUMNS, b8 = 10, 5
b9 = [
    "..........",
    "...
    "..
    ".....
    ".........."
]
b10 = (0, 0)
b3 = fonk1(b9, b10)
if b3:
    print("Path to goal:", b3)
else:
    print("No b3 found")