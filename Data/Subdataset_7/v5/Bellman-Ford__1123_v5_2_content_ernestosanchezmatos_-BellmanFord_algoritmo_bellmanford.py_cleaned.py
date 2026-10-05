import math
b1 = {
    "a": [math.inf, ""],
    "b": [math.inf, ""],
    "c": [math.inf, ""],
    "d": [math.inf, ""],
    "e": [math.inf, ""],
    "f": [math.inf, ""],
    "g": [math.inf, ""]
}
b2 = [
    ["a", "b", 9],
    ["a", "c", 2],
    ["b", "c", 6],
    ["b", "e", 1],
    ["c", "f", 9],
    ["d", "b", 3],
    ["d", "c", 2],
    ["d", "e", 5],
    ["d", "f", 6],
    ["e", "f", 3],
    ["e", "g", 7],
    ["f", "g", 4]
]
def fonk1(origin, destination, value):
    if value < b1[destination][0]:
        b1[destination][0] = value
        b1[destination][1] = origin
        return True
    return False
b3 = "a"
b4 = "g"
b1[b3][0] = 0
while True:
    b5 = True
    for edge in b2:
        origin, destination, b6 = edge
        if fonk1(origin, destination, b1[origin][0] + b6):
            b5 = False
        if fonk1(destination, origin, b1[destination][0] + b6):
            b5 = False
    if b5:
        break
b7 = [b4]
while True:
    b8 = b7[-1]
    if b8 = = b3:
        break
    b7.append(b1[b8][1])
print(f"The shortest path from node '{b3}' to node '{b4}' is: {b7[::-1]}")