import statistics
from operator import itemgetter
import time
def fonk1(filename):
    b1 = []
    with open(filename, "r") as file:
        for line in file:
            x, b2 = map(float, line.split(","))
            b1.append((x, b2))
    return b1
def fonk2(quadrant, output_filename):
    with open(output_filename, "w") as file:
        b3 = len(quadrant)
        for index, point in enumerate(quadrant):
            x, b2 = point
            b4 = []
            for j in range(1, (b3
                b5 = [
                    (index + j) % b3,
                    (index - j) % b3
                ]
                for neighbor in b5:
                    nx, b6 = quadrant[neighbor]
                    b7 = ((nx - x) ** 2 + (b6 - b2) ** 2) ** 0.5
                    b4.append((nx, b6, b7))
            b4.sort(b8 = itemgetter(2))
            b9 = b4[:10]
            b10 = f"{x},{b2} " + " ".join(f"{cx},{cy}" for cx, cy, _ in b9)
            file.write(b10 + "\n")
def fonk3(b1):
    b11 = [point[0] for point in b1]
    b12 = [point[1] for point in b1]
    return b11, b12
def fonk4(b1):
    b11, b12 = fonk3(b1)
    b13 = statistics.median(b11)
    b14 = statistics.median(b12)
    q1, q2, q3, b15 = [], [], [], []
    for point in b1:
        x, b2 = point
        if x <= b13 and b2 >= b14:
            q1.append(point)
        elif x > b13 and b2 >= b14:
            q2.append(point)
        elif x <= b13 and b2 < b14:
            q3.append(point)
        else:
            b15.append(point)
    return q1, q2, q3, b15, b13, b14
