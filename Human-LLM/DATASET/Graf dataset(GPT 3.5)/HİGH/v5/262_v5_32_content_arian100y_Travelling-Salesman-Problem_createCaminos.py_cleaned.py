from operator import itemgetter
import statistics
import time as ti
b1 = ti.clock()
def fonk1(filename):
    b2 = []
    with open(filename, "r") as file:
        for line in file:
            b3 = line.split(",")
            b2.append((float(b3[0]), float(b3[1])))
    return b2
def fonk2(quadrant, filename):
    with open(filename, "w") as file:
        b4 = len(quadrant)
        for u in quadrant:
            b5 = set()
            for j in range(1, int(len(quadrant) / 2) + 1):
                b6 = (quadrant.index(u) + j) % len(quadrant)
                b7 = (quadrant.index(u) - j) % len(quadrant)
                x_v1, b8 = quadrant[b6][0], quadrant[b6][1]
                b9 = ((x_v1 - u[0]) ** 2 + (b8 - u[1]) ** 2) ** 0.5
                x_v2, b10 = quadrant[b7][0], quadrant[b7][1]
                b11 = ((x_v2 - u[0]) ** 2 + (b10 - u[1]) ** 2) ** 0.5
                b5.add((b6, x_v1, b8, b9))
                b5.add((b7, x_v2, b10, b11))
            b5 = sorted(b5, key=itemgetter(3))[:10]
            b12 = " ".join([f"{point[1]},{point[2]}" for point in b5])
            file.write(f"{u[0]},{u[1]} {b12}\b4")
def fonk3(b2):
    b13 = [point[1] for point in b2]
    b14 = [point[0] for point in sorted(b2, key=itemgetter(0))]
    return b14, b13
def fonk4(b2):
    b14, b13 = fonk3(b2)
    b15 = statistics.median(b13)
    b16 = statistics.median(b14)
    print("Median b3:", b16, b15)
    q1, q2, q3, b17 = [], [], [], []
    for point in b2:
        x, b18 = point
        if x <= b16 and b18 >= b15:
            q1.append(point)
        elif x > b16 and b18 >= b15:
            q2.append(point)
        elif x <= b16 and b18 < b15:
            q3.append(point)
        elif x > b16 and b18 < b15:
            b17.append(point)
    return q1, q2, q3, b17, b16, b15