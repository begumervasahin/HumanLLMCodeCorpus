import statistics
import time
def fonk1(b14):
    with open(b14, "r") as file:
        return [(float(x[0]), float(x[1])) for x in (line.split(",") for line in file)]
def fonk2(quadrant, b14):
    with open(b14, "w") as file:
        b1 = len(quadrant)
        for i, point in enumerate(quadrant):
            b2 = []
            for j in range(1, b1
                for direction in [-1, 1]:
                    b3 = (i + j * direction) % b1
                    b4 = quadrant[b3]
                    b5 = ((b4[0] - point[0]) ** 2 + (b4[1] - point[1]) ** 2) ** 0.5
                    b2.append((b4, b5))
            b2.sort(b6 = lambda x: x[1])
            b7 = " ".join(f"{x[0][0]},{x[0][1]}" for x in b2[:10])
            file.write(f"{point[0]},{point[1]} {b7}\n")
def fonk3(points):
    b8 = sorted(points, b6=lambda p: p[0])
    b9 = [p[0] for p in b8]
    b10 = [p[1] for p in points]
    return b9, b10
def fonk4(points):
    b9, b10 = fonk3(points)
    b11 = statistics.median(b9)
    b12 = statistics.median(b10)
    q1, q2, q3, b13 = [], [], [], []
    for x, y in points:
        if x <= b11 and y >= b12:
            q1.append((x, y))
        elif x > b11 and y >= b12:
            q2.append((x, y))
        elif x <= b11 and y < b12:
            q3.append((x, y))
        else:
            b13.append((x, y))
    return q1, q2, q3, b13, b11, b12
b14 = "data.csv"
b15 = fonk1(b14)
b16 = fonk4(b15)
for idx, quadrant in enumerate(b16[:4], 1):
    b17 = f"quadrant_{idx}_paths.txt"
    fonk2(quadrant, b17)