import collections
def fonk1(b7, b8):
    b1 = collections.deque([[b8]])
    b2 = set([b8])
    while b1:
        b3 = b1.popleft()
        x, b4 = b3[-1]
        if b7[b4][x] == b5:
            return b3
        for x2, y2 in ((x+1, b4), (x-1, b4), (x, b4+1), (x, b4-1)):
            if 0 <= x2 < columns and 0 <= y2 < b6 and b7[y2][x2] != wall and (x2, y2) not in b2:
                b1.append(b3 + [(x2, y2)])
                b2.add((x2, y2))
wall, clear, b5 = "
columns, b6 = 10, 5
b7 = ["..........",
        "...
        "..
        ".....
        ".........."]
b8 = (0, 0)
b3 = fonk1(b7, b8)
if b3:
    print("Path to b5:", b3)
else:
    print("No b3 found")